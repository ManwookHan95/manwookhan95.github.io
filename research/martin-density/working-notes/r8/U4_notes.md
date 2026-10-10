# U4 notes (Round 8): consistency audit of the whole chain — the final operator T_final, hypothesis check, current master theorem

Part files: r8/U4_part0.md (reading digest), U4_part1.md (T_final, admissibility, conflicts), U4_part2.md (hypothesis audit),
U4_part3.md (master theorem), U4_part4.md (numerics); scripts r8/U4_work/{tu_mu_check.py, rr_check.py} with outputs *.out.
This file supersedes the part files where they differ.  Numbering/notation: paper/martin_density_note.tex ("the note"); Rounds 5-7
notes with their referee fixes.  Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  No counterexample is claimed or suggested.

## 0. Summary
(1) ONE admissible operator T_final with base U_final (Section 1) carries every design feature used by the refereed results of
    Rounds 5-7: SLD (def:SLD) with bounded-gap signature sets S_l = {2^l(2i+1)}, allowedness (a), (b), (c); a DIAGONAL base with
    super-exponentially decaying entries mu_s = 2^{-s^2-1} (D^mu); private bank/pull coordinates; pigeonhole sub-windows; the full rate
    scheme (V1 (R1)-(R7), V2's minors and shift-pinning rates); b(w) a design power of T_lo(w); one Design(l) dominating every design
    factor; V4's (SF*), (SF_tau), (b'), (Z0), (GM), (FD) in V4-ref R6 order; N-independence.  The recursion is well founded (Lemma W),
    T_final satisfies the conclusion of Martin's Lemma B (Theorem 2.2), and every conflict between the Round-5-7 designs is resolved
    (Section 3).  Two genuine (easily fixed) defects of the literal union were found:
      C1: V1's design factor 8^{sigma(l)} (calibrated to the base 2^{-j}) does NOT dominate the bank/pull factor for the base mu_s needed
          by V3's Theorem RS; FIX: B_mu(l) := 2^{sigma(l)}/mu_{sigma(l)}^2 in Design(l).  (The base 2^{-j} cannot be kept: with it the raise
          room (RR) of Theorem RS fails for every support-swallowing profile |a_s| ~ v_l(s)^{1+b} with b >= 2.)
      C7: V4's (GM) imposed at l = 1 forces c_1 <= 1/60 < 1, contradicting "norm one" in Lemma B and the equality clause of (T-a);
          FIX: (GM) only for l >= 2 (its only use, V4 Lemma 3.4, concerns large l).
(2) Every result in the dependency trees of Master Theorem II (V1), Master Theorem III' (V2-ref) and Theorem RS' (V3 + V3-ref) has its
    hypotheses satisfied by T_final (Section 4, with the window meta-lemma GW); no tree uses the explosive window function, lacunary
    signature sets, or any feature T_final lacks.  Re-verified here: V3-ref's Lemma VP', the logic of Master Theorem III', Theorem RS' on
    sub-windows, V1 Lemma DR/TU constants for the mu-base (with numerics).
(3) CURRENT MASTER THEOREM (Section 5): for T_final, every N and every first row f of p_N:
    (i) F finite: f in Rec_N unless (C*) [near-exact coherent shift resonance at every clean sub-window of all large levels]; block-tame
        rows and R_0, R_0^±, R_S are in Rec_N regardless; constant-sign maximal contact never satisfies (C*);
    (ii) F infinite: f in Rec_N under RS' [(W*), (H2), (H3-inf), (B_fin), (ND'), (RR)], under R1 [(CS_B) instead of (ND'), (RR)], and in
        the classes of Y3 Theorems 3.5, 5.1 and Z5 T6, T7;
    (iii) residual: (C*) \ (BT) at finite F; failure of all criteria of (ii) at infinite F, i.e. (E1) mu-thin supports, (E2) infinitely
        many bad carriers, (E4) (ND') or (H3-inf) failure, (E5) (W*) or (H2) failure (finite-F core at infinite F);
    (iv) density for p_N <=> Lemma Z <=> the residual rows are in Rec_N: OPEN; density for Martin's p built with T_final follows from
        density for infinitely many p_N (lem:martintail; T_final is N-independent), but NO row-wise statement transfers to p: OPEN.
    No SKETCH result lies on the critical paths of (i) and (ii).

| # | Result | Label | Where |
|---|---|---|---|
| 1 | Definition of T_final, U_final (R6 order: target, signature size, weight, level data, sub-windows) | definition | 1 |
| 2 | Lemma W: the recursion is well founded, all constants finite/positive, nothing depends on N | PROVED | 2.1 |
| 3 | Theorem 2.2: T_final admissible; Martin's Lemma B conclusion; (P1), (P2), sub-window (P3); V2's (2.1) | PROVED | 2.2 |
| 4 | Theorem 2.3: feature list (F1)-(F11) | PROVED | 2.3 |
| 5 | Conflicts C1-C9 and their resolution (C1, C7 are new defects with fixes) | PROVED | 3 |
| 6 | Lemma GW (generic window use) and the dependency tables of MT II, MT III', RS' | PROVED (meta-argument; inspection) | 4 |
| 7 | Re-verification of VP', MT III' logic, RS' on sub-windows, DR/TU for the mu-base | PROVED | 4.4 |
| 8 | Master Theorem (i)-(iv) for T_final | PROVED (assembly of refereed results); density OPEN | 5 |
| 9 | Status flags: SKETCH / inspection / single-referee dependencies | — | 6 |
| 10 | Numerics: Lemma TU with s_j = 2^{-beta j^2}; (RR) exponents for the two bases | evidence | 7 |

## 1. The final operator
### 1.1 The base U_final (V3 3.1, design D^mu)
H := l_2 with orthonormal basis (k_s)_{s>=1}; mu_s := 2^{-s^2-1}; U k_s := mu_s e_s.  U is compact (diagonal, mu_s -> 0) with range
containing c_00 (dense), U^* e_s^* = mu_s k_s, U^* is injective on l_1, ||U|| = mu_1 = 1/4, and q^*(a) = ||a||_1 + (sum_s mu_s^2 a_s^2)^{1/2}.
By prop:smooth(c) (valid for every compact dense-range U; its proof uses only injectivity of U^*), NA((c_0,q)) = c_00.
Diagonal identities (PROVED by direct computation; they are all that the diagonal-base arguments use): for b in l_1 and s notin supp b,
<U^*b, k_s> = mu_s b_s = 0; for A = a + sum_{s in J} c_s e_s^* with J ∩ supp a = {}, U^*A = U^*a + X, X := sum_J c_s mu_s k_s ⊥ U^*a,
||U^*A||^2 = ||U^*a||^2 + ||X||^2 and <U^*u, X> = sum_J c_s mu_s^2 u(s) (u in l_1).

### 1.2 Data fixed in advance
 (i)   A ladder bijection j : N x N -> N with j(k,m) < j(k',m) for k < k'; (k(l), m(l)) := j^{-1}(l); then k(1) = 1.
 (ii)  j_0 := 1; S_l := {2^l(2i+1) : i >= 1} (l >= 1): pairwise disjoint, infinite, consisting of even numbers (so j_0 notin S_l), with
       BOUNDED GAPS G_l := 2^{l+1} and min S_l = 3 * 2^l.  Z_0 := N \ union_l S_l = {odd numbers} ∪ {2^r : r >= 1}.
 (iii) h_l := sum_{s in S_l} 2^{-s} e_s^*, H_l := ||h_l||_1, delta^max_l := min{2^{-l}, (4(1 + ||U||)H_l)^{-1}}.
 (iv)  tau_l := 2^{-l} (decreasing to 0).
 (v)   Targets (y^(i))_{i>=1} in c_00 ∩ S_{q^*}, dense in S_{q^*}, with y^(1) := e_1^*/q^*(e_1^*) and containing the (Z0)-targets
       y^* := (e_3^* - e_5^*)/q^*(e_3^* - e_5^*) and y^** := (e_7^* - e_9^*)/q^*(e_7^* - e_9^*)  (3, 5, 7, 9 are odd, hence in Z_0).
 (vi)  Schedule: K_FD := {2^r : r >= 1}; N \ K_FD = {k_1 < k_2 < ...}; (i_r)_{r>=1} a sequence in which every positive integer occurs
       infinitely often.

### 1.3 The recursion; stage l = 1, 2, ... (given everything of the earlier stages)
 (1) TARGET.  If k(l) in K_FD: y_l := e_{j_l}^*/q^*(e_{j_l}^*), j_l := the least odd integer > max(9, max union_{l'<l} supp y_{l'}) (a fresh
     coordinate of Z_0: the (FD) target).  Otherwise k(l) = k_r, and y_l := y^(i_r) if it is ALLOWED at l, i.e.
       (a) supp y^(i_r) ∩ S_{l'} = {} for every l' >= l,     (c) supp y^(i_r) ∩ S_{l'} ⊂ [1, l] for every l' < l,
     and y_l := y^(1) otherwise.  (Targets supported in Z_0, e.g. y^(1), y^*, y^**, FD targets, are allowed at every l.)
 (2) SIGNATURE SIZE.  delta_1 := delta^max_1.  For l >= 2: g_l := delta^max_l H_l/(32 * 3^{|supp y_l|}) and delta_l := the largest delta
     in [delta^max_l/2, delta^max_l] such that |sum_j sigma_j y_l(j) + eps delta H_l| >= g_l for all sigma in {-1,0,1}^{supp y_l} and
     eps = +-1 ((GM)).  [The excluded set is a union of at most 2 * 3^{|supp y_l|} open intervals of length 2g_l/H_l, of total length
     <= delta^max_l/8 < delta^max_l/2; the admissible set is a nonempty compact set, so the maximum exists.]
 (3) n_l := q^*(y_l + delta_l h_l), u_l := (y_l + delta_l h_l)/n_l, v_l := delta_l h_l/n_l, delta°_l := delta_l H_l/n_l,
     eta_l := min(1, min_{j in supp y_l} |y_l(j)|), Lambda°(l) := prod_{l''<=l}(1 + 2/delta°_{l''}).
 (4) WEIGHT.  c_1 := 1.  For l >= 2, c_l := the minimum of the positive numbers
     (W1) c_{l-1}/4;   (W2) b(l-1, M(l-1))^2;   (W3) (delta_l H_l)^2;
     (W4) tau_{l'} 2^{-2s} c_{l'} delta_{l'}/2 for l' < l and s in supp y_l ∩ S_{l'}   (allowedness (b) and V4's (b'));
     (W5) c_{l-1} delta_l 2^{-min S_l - l - 10}/(1 + ||U||)   ((SF*), second half);
     (W6) g_l 2^{m(l) + k(l) - l}   ((GM): Phi_l <= g_l 2^{-l});
     (W7) 3 * 2^{-10} tau_{l-1} lambda_{l-1} delta_{l-1} 2^{-(m(l-1) + k(l-1) + min S_{l-1})} eta_{l-1}/(n_{l-1}(1 + ||U||))   ((SF_tau)).
     Phi_l := 2^{-m(l)-k(l)} c_l, lambda_l := m(l) Phi_l.
 (5) LEVEL DATA.  T(l) := union_{l''<=l} supp y_{l''}; s_max(l) := max(T(l) ∪ {1}); sigma(l) := max_{l''<=l} min(S_{l''} ∩ (s_max(l), inf))
     (<= s_max(l) + 2^{l+1}); m^nat_{l''}(l) := ||v_{l''} 1_{S_{l''} \ ([1,l] ∪ T(l))}||_1 > 0 (l'' <= l); D(l) := 1 + sum_{l''<=l}
     (1/m^nat_{l''}(l) + 1/Phi_{l''}); delta_min(l) := min_{l''<=l} delta_{l''}; G(l) := 2^{l+1};
       B_mu(l) := 2^{sigma(l)}/mu_{sigma(l)}^2 = 2^{2 sigma(l)^2 + sigma(l) + 2};
     G^*(l) (Z4), H_comb(l) (Z6), G^**(l) (Y1 1.2), Xi^Y(l) := [l H_comb G^** D]^8 (l 2^{l^3} Lambda° G^**)^5 (Y2); the patterns of level l
     (V1 2.6, with the kept set as in V2-ref 3), their zero-cost cones and normalized extreme rays, H_tune(l) (V1 1.2); the shift patterns
     pi (V1 2.5) and the enlarged shift patterns kappa^sh (V2-ref P3); the determinantal objects O = (kappa, J, K) and polynomials pi_O
     (V2 Def. 2.1); Lip(l) >= 1, C_L(l), N_L(l) (V2 Lemma L for {pi_O : O of level <= l}, with V2's choice rule), delta_comb(l) (least
     nonzero design minor; 1 if none), C_*(l) := |T(l)| + 2, delta_sh(l) (V2 Cor. C1.1 with the weights m^d of V2-ref P4; 1 if none),
     rows(l), cols(l).  RATE OBJECTS of level l: V1's (R1)-(R7), the determinantal objects, the shift-pinning objects (kappa^sh, sh);
     omega(l) := their number.
       Design(l) := [ l 2^{l^3} B_mu(l) 2^{s_max(l)} 2^{G(l)} delta_min(l)^{-1} Lambda°(l) (1 + |T(l)|) D(l) G^*(l) H_comb(l) G^**(l)
                      H_tune(l) Xi^Y(l) ]^6 x Lip(l) (2 + 1/delta_comb(l)) (rows(l) cols(l))^l C_*(l) C_L(l) (1 + 1/delta_sh(l)).
 (6) SUB-WINDOWS.  M(l) := omega(l) + 1; for w = (l,i), 1 <= i <= M(l), with lexicographic predecessor w^-:
       u(w) := 1/4 (w = (1,1)), u(w) := b(w^-) otherwise;  Q(w) := (4 Design(l)/u(w))^{omega(l)+20};  n(w) := ceil(l 2^{l^3} Q(w));
       T_hi(w) := min{T_lo(w^-), 2^{-l^3}/(l Q(w))} (T_lo((1,1)^-) := 1);  T_lo(w) := 2^{-n(w)} T_hi(w);
       eta(w) := T_lo(w)^4/(l Design(l));  b(w) := min{eta(w), (eta(w)/C_L(l))^{N_L(l)/2}}/(1 + Lip(l) C_*(l)).
     W(w) := [T_lo(w), T_hi(w)] with its n(w) dyadic scales; Band(w) := (b(w), u(w)).
(D2) T_final e_{k,m} := c_{j(k,m)} u_{j(k,m)}, extended linearly and continuously to l_1(N x N).

## 2. Well-foundedness, admissibility, features
### 2.1 Lemma W.  PROVED.
(a) Every quantity of stage l is a function of the data of 1.2, of quantities of earlier stages and of earlier steps of stage l.
(b) All quantities used as divisors are finite and positive.  (c) Nothing depends on N.
Proof.  (a) (1) uses supports of y_{l'} (l' < l), the fixed S_{l'} and the schedule (allowedness is now (a) and (c) only, both support
conditions); (2) uses y_l; (3) uses y_l, delta_l; (4) uses c_{l'}, delta_{l'}, y_{l'}, n_{l'}, eta_{l'} (l' < l), b(l-1, M(l-1)) (step (6) of
stage l-1), delta_l, H_l, g_l, y_l; (5) uses data of index <= l, including c_l; the patterns, cones, rays, Hoffman constants, the
polynomials pi_O and the Lojasiewicz constants depend only on the finitely many numbers u_{l''}(j) (l'' <= l, j in T(l)), Phi_{l''},
m^nat_{l''}(l) and on finitely many sign/contact/status choices; (6) uses Design(l), omega(l), C_L(l), N_L(l), Lip(l), C_*(l) and the
predecessor values T_lo(w^-), b(w^-).  The (SF_tau) requirement on the weights after level l (a statement about the future) is imposed at
stage l+1 by (W7) and propagated by (W1): sum_{l''>l} lambda_{l''} <= sum_{l''>=l+1} c_{l''}/4 <= c_{l+1}/3.
(b) m^nat_{l''}(l) > 0 because S_{l''} \ ([1,l] ∪ T(l)) is infinite; c_l > 0 as the minimum of finitely many positive numbers ((W4) is a
finite list since supp y_l is finite); g_l > 0; delta_comb, delta_sh > 0 by definition; the Hoffman constants are finite; C_L, N_L exist
by the Lojasiewicz inequality (Bochnak-Coste-Roy, Cor. 2.6.7), as in V2 Lemma L.
(c) Patterns, objects and maxima run over subsets of [1, l] and over the blocks m(l'') of carriers l'' <= l.  For p_N, rate objects
involving carriers with m(l'') > N take the value 1 (V1-ref p0); row constructions with owners use L_N := {l : m(l) <= N} and
o_N(j) := min{l in L_N : u_l(j) != 0} (V4-ref R3); both concern rows, not T_final.  QED

### 2.2 Theorem 2.2 (admissibility; Martin's Lemma B).  PROVED.
(a) (T-a) q^*(T e_{k,m}) = c_{j(k,m)} <= 1 = c_1; (T-b) T_final is injective; (T-c) Y := T_final(l_1(N x N)) satisfies Y ∩ c_00 = {0};
    (T-d) for every m, {u_{j(k,m)} : k in N} is norm dense in S_{q^*}.
(b) ||T_final|| = 1; T_final is injective; Y is a separable operator range, dense in (l_1, q^*) = (c_0, q)^*, with Y ∩ NA((c_0,q)) = {0};
    for every m the normalized vectors T e_{k,m}/q^*(T e_{k,m}) = u_{j(k,m)} are dense in S_{q^*}, hence in S_Y: the conclusion of
    Martin's Lemma B (and everything Martin's proof uses about T, rem:lemmaB of the note).
(c) (P1) y_l in c_00, ||y_l||_1 <= 1, n_l in [3/4, 5/4], supp y_l ∩ S_{l'} = {} (l' >= l); for s in S_l: u_l(s) = v_l(s) = delta_l 2^{-s}/n_l,
    u_{l'}(s) = 0 (l' < l), u_{l'}(s) = y_{l'}(s)/n_{l'} (l' > l).  (P2) sum_{l'>l} c_{l'} <= (4/3) c_{l+1}, sum_{l'>l} lambda_{l'} <= c_{l+1}/3
    <= b(l, M(l))^2/3.  Sub-window (P3): for every w = (l,i): T_hi(w) l 2^{l^3} Q(w) <= 1; n(w) >= l 2^{l^3} Q(w) >= l 2^{l^3} Design(l) >=
    l 2^{l^3} Lambda°(l); T_hi(w^+) <= T_lo(w); b(w) < u(w); u(w^+) = b(w); the bands are pairwise disjoint; sum_{l'>l} lambda_{l'} <=
    b(w)^2/2 <= T_lo(w)^8.
(d) (V2's (2.1)) beta(w) := (1 + Lip(l) C_*(l)) b(w) <= eta(w) < 1/C_L(l) and C_L(l) beta(w)^{2/N_L(l)} <= eta(w); moreover
    Design(l)^k T_lo(w) <= u(w)/8 for k <= 4 and l large.
Proof.  (T-a): q^*(u_l) = 1, and c_l <= c_1 = 1 by (W1).  (P1): q^*(y_l) = 1 >= ||y_l||_1; q^*(delta_l h_l) <= (1 + ||U||) delta_l H_l <= 1/4
since delta_l <= delta^max_l, so n_l in [3/4, 5/4]; the support statement is allowedness (a) (targets supported in Z_0 meet no S); on S_l
the other signatures vanish (disjointness) and targets y_{l'}, l' <= l, vanish by (a).  (P2): (W1) gives c_{l'+1} <= c_{l'}/4, and
lambda_{l'} = m 2^{-m-k} c_{l'} <= c_{l'}/4 (k, m >= 1); (W2) gives c_{l+1} <= b(l, M(l))^2.
(T-b), (T-c) (the proof of thm:SLD): let x in l_1(N x N), indexed by l, with Z := T x = sum_l x_l c_l u_l in c_00, and x_{l'} != 0.  For
s in S_{l'}, Z(s) = x_{l'} c_{l'} delta_{l'} 2^{-s}/n_{l'} + sum_{l>l', s in supp y_l} x_l c_l y_l(s)/n_l by (P1).  If the last sum is non-empty
with least index L(s), (W4) at stage L(s) (tau <= 1) gives 2 c_{L(s)} <= 2^{-2s} c_{l'} delta_{l'}, so the sum is at most
(4/3)||x||_inf sum_{l>=L(s)} c_l <= (16/9)||x||_inf c_{L(s)} <= (8/9)||x||_inf 2^{-2s} c_{l'} delta_{l'}; hence |Z(s)| >= c_{l'} delta_{l'} 2^{-s}
(|x_{l'}|/n_{l'} - (8/9)||x||_inf 2^{-s}) > 0 for all large s in S_{l'}, contradicting Z in c_00.  So x = 0.
(T-d): fix m, i.  supp y^(i) is finite and meets finitely many S_{l'}, so y^(i) satisfies (a) and (c) at every l >= l_i := 1 + max(supp
y^(i) ∪ {l' : S_{l'} ∩ supp y^(i) != {}}).  As i occurs infinitely often in (i_r) and j(., m) is strictly increasing, y_l = y^(i) for
infinitely many l = j(k_r, m) (k_r notin K_FD); along them |n_l - 1| <= q^*(delta_l h_l) <= (5/4) 2^{-l} H_l and q^*(u_l - y^(i)) <=
|1/n_l - 1| + q^*(delta_l h_l)/n_l -> 0.  Density of (y^(i)) gives density of {u_{j(k,m)} : k}.
(b): the domain is l_1(N x N), so ||T|| = sup q^*(T e_{k,m}) = c_1 = 1 (attained at j^{-1}(1)); Y is the range of a bounded operator on a
separable space; the closure of the subspace Y contains a dense subset of S_{q^*}, hence the unit ball, so Y is dense; Y ∩ c_00 = {0} is
(T-c) and NA((c_0,q)) = c_00 (prop:smooth(c)); density of the normalized vectors is (T-d).
(c), sub-window part: T_hi(w) <= 2^{-l^3}/(l Q(w)) and n(w) >= l 2^{l^3} Q(w) by (6); Q(w) >= Design(l) >= Lambda°(l) (u <= 1/4, all factors
>= 1); T_hi(w^+) <= T_lo(w) by (6), also across levels.  b(w) <= eta(w) <= T_lo(w)^4 <= 2^{-4n(w)}, and n(w) >= Q(w) >= (4/u(w))^{20} >=
16/u(w), so b(w) <= 2^{-64/u(w)} < u(w) (u <= 1/4); u(w^+) = b(w) by definition, and consecutive open intervals of a decreasing sequence
are disjoint.  b decreases along the sub-windows of a level, so sum_{l'>l} lambda_{l'} <= b(l, M(l))^2/3 <= b(w)^2/2 <= T_lo(w)^8.
(d): beta(w) <= min{eta, (eta/C_L)^{N_L/2}}, so C_L beta^{2/N_L} <= eta; eta(w) <= T_lo(w)^4 <= 2^{-4 l^3} < 1/Design(l) <= 1/C_L(l).  For the
last claim: T_lo(w) <= 2^{-n(w)} <= 2^{-4 Design(l)/u(w)} and Design^k 2^{-4 Design/u} <= u/8 once Design(l) >= 8k (V2 Lemma 2.1).  QED

### 2.3 Theorem 2.3 (features).  PROVED.
T_final, U_final have: (F1) the SLD structure (D0), (D1)(a),(b), (D2) with (P1)-(P3) per sub-window; (F2) bounded gaps and allowedness (c)
(Y3 D_sigma); (F3) a diagonal base with positive entries (V1, V2, Y4-ref, V4) and mu_s = 2^{-s^2-1} (V3 D^mu); (F4) private bank and pull
coordinates (all far coordinates of every S_l, bounded gaps); (F5) pigeonhole sub-windows M(l) = omega(l)+1, u(w) = b(w^-), Q(w) =
(4 Design/u)^{omega+20}; (F6) the rate scheme of Y1, V1 (R1)-(R7), V2 (minors, shift-pinning rates with enlarged patterns); (F7) b(w) a design
power of T_lo(w) absorbing the Lojasiewicz exponent; (F8) Design(l) >= each of G^*, H_comb, D(l), G^**, Xi^Y (hence Xi' of D''' and the
SLD_G factor), 2^{s_max}/delta_min, 2^{G(l)}, H_tune, B_mu (>= 8^{sigma}, >= Y1's 2^{sigma}), Lip, 1/delta_comb, (rows cols)^l, C_*, C_L,
1/delta_sh, |T(l)|; (F9) c_{l+1} <= c_l/4, <= b(l, M(l))^2 (<= T_lo(l, M(l))^3), <= (delta_{l+1} H_{l+1})^2; (F10) V4's (SF*), (SF_tau) with
tau_l -> 0, (b'), (Z0), (GM) for l >= 2, (FD), in V4-ref R6 order; (F11) N-independence.
Proof.  (F1)-(F9), (F11): Theorem 2.2, Lemma W and the definitions.  (F10): (SF_tau) for level l is (W7) at stage l+1 with (P2):
(1 + ||U||) sum_{l''>l} lambda_{l''} <= (1 + ||U||) c_{l+1}/3 <= 2^{-10} tau_l lambda_l delta_l 2^{-(m(l)+k(l)+min S_l)} eta_l/n_l, which implies
(SF*) (tau <= 1); the second half of (SF*) is (W5); (b') is (W4); (GM) for l >= 2 is (2) with (W6); (Z0) is 1.2(v); (FD): every block m has
the infinitely many stages l = j(2^r, m), r >= 1, where y_l = e_{j_l}^*/q^*(e_{j_l}^*) with j_l odd (in no S_i) and fresh (in no supp y_{l'},
l' < l), so u_{l'}(j_l) = 0 for l' < l, i.e. j_l is owned by l (and o_N(j_l) = l if m <= N), and |y_l(j_l)| = 1/(1 + mu_{j_l}) >= 4/5 >
(1 + ||U||)(||y_l||_1 - |y_l(j_l)| + delta_l H_l) = (5/4) delta_l H_l, because delta_l H_l <= 1/(4(1 + ||U||)) = 1/5.  QED

## 3. Conflicts between the Round-5-7 designs and their resolution (each PROVED unless stated)
C1 (two diagonal bases: s_j = 2^{-j} in V1/V2; mu_s = 2^{-s^2-1} in V3).  RESOLVED: U_final is the mu-base and Design(l) contains
  B_mu(l) instead of 8^{sigma(l)}.  [New defect of the literal union, found here.]
  (i) The note, Z3 Theorem E / Lemma U / Lemma 3.1 (it uses only the clamp formula at zhat, zhat^#), Y4 Lemmas 2.2, 2.3, V3 Lemmas
  2.1-2.3 and Theorem 2.5 hold for every compact dense-range U.  (ii) The diagonal-base arguments (Y4-ref C.1-C.7, V1 Lemmas B, DR, TU,
  CO, ST, Corollary AC, V2 Theorem B, V3-ref Lemma VP', V4 Theorems 2.2, 3.5, 5.6, Proposition 5.3) use only the identities of 1.1 with
  general entries, plus a lower bound for s_j^2 v_l(j) at bank coordinates.  (iii) That lower bound is the ONLY place where the value
  2^{-j} enters: V1 Lemma DR(ii) and Lemma TU use s_s^2 v_c(s) >= 8^{-sigma(l)} delta_min(l)/2 >= Design(l)^{-1/6} for bank coordinates
  s <= sigma(l).  For U_final, mu is decreasing and v_c(s) = delta_c 2^{-s}/n_c >= (4/5) delta_min(l) 2^{-sigma(l)}, so
        mu_s^2 v_c(s) >= (4/5) delta_min(l)/B_mu(l) >= Design(l)^{-1/6}     (Design(l)^{1/6} >= l 2^{l^3} B_mu(l)/delta_min(l)),
  which is exactly the inequality V1 uses.  Consequences, re-derived: the donor bank mass mu^D = 2 nu Lam/(lambda_c mu_s^2 v_c(s)) <=
  2 nu D(l) (5/4) B_mu(l) Lam/delta_min(l) <= Design(l) Lam (lambda_c >= 1/D(l), nu <= ||U|| = 1/4); the second-order remainder of V1
  Lemma B(ii) is <= (||U|| + mu^D/nu) ||X||^2/nu^2 with ||X|| <= mu^D mu_s <= Design Lam, i.e. <= C Design^2 Lam^2 << Lam/lambda_c; in
  Lemma TU the contraction bound |Phi'| <= C |L_0| Design (eta + kappa)(eta + ||U||) <= 1/2 holds for eta <= c_T = f-constant x
  Design^{-3}, as in V1.  (iv) ||U|| = 1/4 <= 1/2 wherever V1/V3 assume ||U|| <= 1/2.
  (v) The mu-base is FORCED by V3: (RR_W) requires M^W_mu(y) = sum{mu_s W_s : |a_s| < y W_s} = O(y^{1+eps}).  For W = v_l on a bounded-gap
  signature set and |a_s| = 2^{-(1+b)s}, the active set is {s > log_2(1/y)/b}; with entries 2^{-s} this gives M ~ y^{2/b}, so (RR) fails
  for every b >= 2; with mu_s = 2^{-s^2-1}, V3 Lemma 3.1(b) gives (RR) for every b > 0 (numerics: Section 7).
  (vi) Why the literal V1 factor does not suffice: sigma(l) > s_max(l) is governed by the supports of the coarse targets, which belong to
  an arbitrary dense family and may contain coordinates of Z_0 far beyond anything fixed at earlier stages; with rule (c), allowedness (b)
  only involves coordinates s <= l, so no factor of V1's Design(l) is forced to exceed 2^{2 sigma(l)^2}, while mu_{sigma}^2 v(sigma) <=
  2^{-2 sigma^2 - 2 - sigma}.  Thus V1's "s'^2 v' >= Design^{-1/6}" can fail for the mu-base unless B_mu(l) is put into Design(l).
C2 (order of choices: the note fixes c_l before y_l; V4's (GM), (SF*), (b') need y_l and delta_l before c_l).  RESOLVED by V4-ref R6's order
  (1.3).  Every result uses allowedness (b) only as a property of the pair (y_l, c_l), which (W4) guarantees; (T-d) only needs that every
  target is eventually allowed, which is easier when (b) is enforced through c_l; no result uses a lower bound on c_l except through
  design factors (D(l) via 1/Phi, Lambda°, Design) that are computed after c_l.
C3 (three formulas for c_{l+1}: V1 min{c_l/4, b^2, (delta H)^2}; V2 min{c_l/4, T_lo^3, b^2}; V4 extra upper bounds).  RESOLVED by (W1)-(W7)
  (b(l,M(l))^2 <= T_lo(l,M(l))^8 dominates V2's T_lo^3 term); each result uses its own term only as an upper bound.
C4 (two choices of b(w): V1's T_lo^4/(l Design), V2's Lojasiewicz-adjusted value).  RESOLVED by V2's (smaller) b.  V1's estimates use only
  b(w) <= T_lo(w)^4/(l Design(l)) and disjointness of bands; b enters lower bounds only through u(w^+) = b(w) inside Q(w^+), computed after.
C5 (Z3-ref's explosive window function (D1^F); V4 Lemma 2.6's lacunary signature sets).  RESOLVED by pigeonhole sub-windows and bounded
  gaps; neither alternative is used by any result in the dependency trees of Section 4 (the explosive design appears only in Z3-ref part 4,
  Y4-ref A.1 and Y2 6.4 (SKETCH); Y1's "explosive ladder of sub-windows" IS the pigeonhole recursion).  V4 Lemma 2.6 (a statement about
  lacunary designs) does not hold for T_final and is not claimed; (O4-crit) is settled for T_final by D^mu + Theorem RS' instead.
C6 ((FD) targets differ across blocks, so Martin's "same target sequence in every block" is lost at the FD stages).  Harmless: only
  (T-a)-(T-d) are used (rem:lemmaB), and (T-d) holds per block.  (FD) serves only the NEGATIVE V4 Proposition 5.8 and may be dropped
  without affecting any positive statement.
C7 ((GM) at l = 1 versus norm one).  [New defect, found here.]  S_1 = {6, 10, 14, ...}, H_1 = 1/60, delta^max_1 = 1/2.  (GM) with sigma = 0
  requires g_1 <= delta_1 H_1 <= 1/120, and Phi_1 = 2^{-m(1)-k(1)} c_1 <= g_1/2 then forces c_1 <= 2^{m(1)+k(1)}/240, e.g. c_1 <= 1/60 if
  j(1,1) = 1.  So V4-ref R6 read literally at l = 1 gives ||T|| < 1, violating "norm one" in Lemma B and the equality clause of (T-a).
  FIX: impose (GM) only for l >= 2 and put c_1 := 1.  This suffices: (GM) is used only in V4 Lemma 3.4, whose conclusion concerns
  carriers l > log_2(2 Theta) + 1 >= 2.  (Rescaling T by 1/c_1 would instead break (GM) at later stages.)
C8 (V3's Theorem RS' is stated over "SLD, D_sigma, SLD_G, D''', D_X, D^PW, D^Y" over the mu-base, not over D_Omega/D^{V2}).  RESOLVED in 4.3:
  its window use is generic, one sub-window per level suffices, and (W*) is a hypothesis relative to l 2^{l^3} Lambda°(l) <= n(w).
C9 (Y3's example "S_l minus {j_0}").  With j_0 = 1 odd, j_0 notin union S_l; no removal needed.

## 4. Hypothesis audit for T_final
### 4.1 Lemma GW (generic window use).  PROVED (meta-argument; the same as V1 Theorem 1'(d), Y1 Theorem 1(d), Y4 Lemma 1.5(c),
refereed for D_X, D^PW, D_Omega).
In every window theorem of Section 8 of the note and of Rounds 5-7, the window enters only through: (i) the dyadic scales of ONE window;
(ii) conditions "T_hi x X_l -> 0" and "n/X_l -> infinity" along the levels used, X_l being C_f^{l^2} times design factors of level l,
times (pigeonhole statements) at most omega(l)+3 factors u^{-1}, times (room statements) a room product Lambda_f, Lambda^±_f or Lambda*_f
that the theorem's hypothesis compares with l 2^{l^3} Lambda°(l); (iii) the box bound sum_{l'>l} |Delta theta_{l'}| <= 6 sum_{l'>l}
lambda_{l'}/t <= 6t^2, needing sum_{l'>l} lambda_{l'} <= T_lo^3 on the window; (iv) T_hi(next) <= T_lo(previous).  For T_final and any
sub-window w of level l these hold by Theorem 2.2(c) and (F8): T_hi(w) <= 2^{-l^3}/(l Q(w)), n(w) >= l 2^{l^3} Q(w), Q(w) >= Design(l)
(4/u(w))^{omega(l)+3}, Q(w) >= Lambda°(l), C_f^{l^2} 2^{-l^3} -> 0, sum_{l'>l} lambda_{l'} <= T_lo(w)^8.  Hence each such theorem holds
for T_final with "the window of level l" read as "any sub-window of level l".  QED

### 4.2 Dependency tree of MASTER THEOREM II (V1 4.3) and III' (V2-ref 4b)
[any T] = valid for every admissible T and every compact dense-range U; [SLD] = uses (P1)-(P3), allowedness (a) (and (b) only inside
thm:SLD); [diag] = diagonal identities; [gaps] = bounded gaps; [sub] = pigeonhole sub-windows; [rate] = rate scheme; [Des] = design factors.
 - Note, Sections 1-7: def:admissible, lem:dualball, lem:threshold, eq:margin, lem:rigidity, prop:forced, prop:smooth(c),
   prop:approximants, prop:reduction, lem:pair, thm:compact, rem:lemmaZ(c), lem:martintail, lem:algebra, lem:base, lem:slack,
   thm:transfer, lem:bookkeeping, lem:TV, lem:transferdata, lem:persistence, def:twopiece, prop:onesidedupper, thm:onesided, def:SC,
   thm:engineered, cor:D1, def:BT, cor:BTrecovered: [any T], I finite.  OK.
 - Note, Section 8, any-T tools: lem:twosided, lem:smallness, lem:budget, lem:suplevel, lem:finitebase, lem:phicalc, lem:switchbudget,
   lem:split, lem:peakshift (eq:peakshift, eq:didentity), lem:flip, lem:boundedfree, lem:uniformtransfer, thm:windowed,
   lem:onesidedtransfer, lem:avgfunctionals.  OK.
 - Note, Section 8, design tools: def:SLD, thm:SLD, R_0, lem:R0, lem:box, lem:pinning, lem:triangular, prop:pinned, def:windowcert,
   prop:windowcert, thm:R0, thm:reductionZ, def:swallowed, lem:modswallow, lem:badpeaks, lem:exactswitch, lem:windowtwopiece, thm:Bpm,
   thm:S: [SLD].  OK by Theorem 2.2 and Lemma GW.
 - Z3 (Round 5, refereed): Theorem E, Lemma U, Lemma 3.1, Lemma 3.2 ("flipped"), Proposition T step (5) with fixes T2-T6: [any T].  OK.
   Z4 Lemma 5.0 (for M-II.3): [any T].  OK.
 - Y1 (Round 6, refereed): Theorems 1, 2, Lemmas T, T2, T3, 3.1-3.6 (constants Y1-ref m2, m5), Proposition 5.2 (structure), Theorem E',
   kind [1'], shift trick, donor bookkeeping: [sub], [rate] (R1)-(R4), [Des] (D(l), G^**, 2^{sigma}, |T(l)|); the rooms on
   S^nat = S \ (F ∪ T(l)) use (P1) and allowedness (a).  OK: T_final's scheme contains (R1)-(R4), M(l) = omega(l)+1 counts all objects,
   B_mu >= 2^{sigma}, Lemma GW.
 - Y2 (refereed): Lemma T(c)-(e), Lemma U', Theorem E', Lemma 5.1 / Proposition 5.2, G^**, Xi^Y: [any T] + [Des].  OK.
 - Y3 Proposition 3.3 (D_sigma): [gaps], allowedness (c).  OK (F2).
 - Y4 (refereed): Lemma 1.8 (convex geometry), Lemma 2.2, Lemma 2.3 ([any T]), Theorem 1.6 ([sub]).  OK.
 - Y4-ref C.1-C.7 (pull effect, pulled supports in Lemma U, data at pulls, two-sided tuning; proved by the Y4 referee, re-verified and
   re-proved with design constants in V1): [diag], [gaps], H_tune.  OK with C1.
 - V1 (Round 7, refereed correct with p0-p5): Theorem 2', classification 2.2, pinning 2.3, Lemma D (uses sum_{l'>l} lambda_{l'} <= b^2/2),
   Lemma 3.4', Lemma S, patterns and rays 2.6, Lemmas B, DR, TU, CO, ST, NS, RR, Proposition TR, Theorem E'', Master Theorem II,
   Corollaries M-II.1-3, AC: [diag], [gaps], [sub], [rate], [Des].  OK, with C1 for DR(ii) and TU (literal 8^{sigma} insufficient).
 - V2 (Round 7, refereed correct with P1-P7): Lemma H, Lemma L (pure algebra); Definition 2.1/2.2, Lemma 2.1, Lemma 2.3 (buffer peaks,
   needs sum_{l'>l} lambda_{l'} <= T_lo(l)^3); Theorem B with P2 (the system of V1's Proposition TR, L_0 = Kp); Corollary B.1; Lemma 3.1,
   Definition 3.2 with P3; Theorem C1 with P7: [rate], [Des], V1 Lemmas TU, ST.  OK (Theorem 2.2(d) is V2's (2.1)).
 - Master Theorem III' (V2-ref 4b): all of the above.  OK.

### 4.3 Dependency tree of THEOREM RS' (V3 3.4 with V3-ref Section 3)
 - V3 Lemmas 2.1, 2.2, 2.3 (raise transfer), Corollary 2.4, Theorem 2.5 (E_RT): [any T], any F.  OK.
 - V3 3.1 (D^mu) and Lemma 3.1 (RR): diagonal base with mu_s = 2^{-s^2-1}.  OK (F3); fails for the base 2^{-j} when b >= 2 (C1(v)).
 - V3-ref Lemma VP' under (ND'_{L_0}): [diag].  OK; re-verified in 4.4(b).
 - Z5-ref Theorem R1 Steps 1-4 (Claims 3.1, 3.2), Lemma R2, Lemma R0; Z5 Lemma 5.2 (T10): R1 [SLD] with windows via (W*); R2, T10 [any T].
 - Note: lem:exactswitch, lem:modswallow, lem:badpeaks (with (H3-inf) via V3-ref 3(b)), lem:persistence, def:swallowed: [SLD].
 - Y3 Theorem 2.1 (raised T8; any admissible T, any F).  OK.
 - Theorem RS' itself: Step 1 needs levels l_j with Lambda*_f(l_j)/(l_j 2^{l_j^3} Lambda°(l_j)) -> 0 ((W*)), n_j = O(Lambda*_f(l_j)) =
   o(n(w_j)) for a sub-window w_j of level l_j (n(w) >= l 2^{l^3} Lambda°(l)), m_j + n_j <= n(w_j) with m_j ~ (2/eps)(2 n_j + log(C/(theta_j
   c_flat^2))), and T_hi(w_j) Lambda*_f(l_j) <= 2^{-l_j^3}/l_j -> 0; Steps 2-6 use the box bound on the sub-window and f-constants.  OK.

### 4.4 Items re-verified here (beyond inspection)
(a) V1 Lemma DR(ii) and Lemma TU for the mu-base: Section 3, C1(iii); numerics in Section 7 (Lemma TU with s_j = 2^{-beta j^2}).
(b) V3-ref Lemma VP' (single-referee item on the RS' path).  Statement: under (ND'_{L_0}) [a|_F notin span{u_k|_F : k in L_0}] there are a
  finite F_0 ⊂ F and c_0, C_0 > 0 such that for every raise Delta a (supp ⊂ F \ F_0, same signs as a) with ||U^*Delta a|| <= c_0 there is
  Delta a'' in l_1(F_0), ||Delta a''||_1 <= C_0 ||U^*Delta a||, |Delta a''_s| <= |a_s|/2, with u_k(zhat^#) = u_k(zhat) (k in L_0) for the row
  with forced data ((a + Delta a + Delta a'')/q^*(.), z).  Proof (re-derived).  For a perturbation supported in F, U^*(a + Delta) is
  supported (in the basis (k_s)) on F, so u(zhat^#) - u(zhat) = <U^*u, e^# - e> = sum_{s in F} mu_s u(s)(e^# - e)_s depends only on u|_F.
  Let V_0 := {c in R^{L_0} : (sum c_k u_k)|_F = 0}; then G(x)_k := <U^*u_k, e(x) - e>, e(x) := U^*(a + Delta a + x)/||U^*(a + Delta a + x)||,
  takes values in V_0^perp.  Differentiating x -> U^*(a + x)/||U^*(a + x)|| at 0: DG(0)xi = Lambda(xi)/nu with Lambda(xi)_k = sum_{s in F}
  mu_s^2 xi_s (u_k(s) - a_s gamma_k/nu^2), gamma_k = <U^*u_k, U^*a>.  A vector c annihilates Lambda(l_1(F)) iff (sum c_k u_k)(s) =
  a_s (sum c_k gamma_k)/nu^2 for all s in F (mu_s != 0), i.e. iff u_c|_F = kappa a|_F; conversely such c has sum c_k gamma_k = <U^*u_c, U^*a>
  = sum_{s in F} mu_s^2 u_c(s) a_s = kappa nu^2.  Under (ND') kappa = 0, so the annihilator is V_0 and Lambda(l_1(F)) = V_0^perp; finitely many
  columns suffice (F_0).  DG(x) depends continuously on (U^*Delta a, x) and has a bounded right inverse near 0; |G(0)| <= ||U|| ||e(0) - e||
  <= 2||U|| ||U^*Delta a||/nu.  The quantitative surjective mapping theorem (Graves) gives x in l_1(F_0) with G(x) = 0 and ||x||_1 <=
  C_0 ||U^*Delta a||; on the finite F_0, |x_s| <= |a_s|/2 once c_0 is small, so the signs on F are kept and z = sgn a^# on F.  Finally
  lambda = q^*(a + Delta) >= 1 + ||Delta a||_1 - ||Delta a''||_1 - ||U^*Delta|| >= 1 for small raises, because ||U^*Delta a|| <= (max of mu_s
  over the active set) ||Delta a||_1 = o(||Delta a||_1).  CONFIRMED.
(c) Master Theorem III' (V2-ref 4b; logic).  V1's proof of Master Theorem II uses (SH_w) only through the shift bound |Delta d_m| M_m <=
  K t (Lemma S -> Step 0 of Proposition TR) and (VR_w) only in Step 3 of Proposition TR (blockwise ray removal).  Theorem C1(I) gives the
  shift bound with K <= C_f Design^3/u^3 when rho^sh >= u.  Theorem B (with the transplant's own system, V2-ref P2) gives a Hoffman
  projection tau' of tau_0 onto Sigma^# including the box rows, with ||tau_0 - tau'||_1 <= C_H^# sum_m |Q^#_m(tau_0)| and C_H^# <=
  C_f^l Design^2/u; Steps 4-5 of Proposition TR use only ||tau - tau'||_1, the sign rows and the box rows tau' <= 12 lambda/t (needed for
  t|b(j)| <= 12 lambda v(j) = mu/2 at pulls and for the kind-[2] bounds), all contained in Sigma^#.  The extra cost C_f Design^2 eta
  log(1/eta), eta = T_lo^4/(l Design), is o(T_lo^2), and the extra value moves 2 eta << c_f Lam keep V1's status table.  Lemma QB and Step 4
  of Theorem B are not needed: in V1's assembly every block containing a near-threshold kept carrier is donor-raised (V2-ref 3(ii)).
  The window arithmetic: K_w <= (room product) x C_f^l Design^2/u x (pinning constants) is absorbed by Q(w).  CONFIRMED.
(d) Hidden N-dependence: V2 Theorem B(d)'s factor (2 A_max)^{-N} is >= 1 since A_m <= m 2^{-m} <= 1/2, so C_H^# <= C_f^l Design^2/u is
  N-free up to the f-constant.  Elsewhere N enters only through f-constants (C_f, l_f), absorbed for each fixed f.  CONFIRMED.
(e) Features NOT used by any of the three trees: the explosive window function (absent from T_final); lacunary signature sets (absent);
  allowedness (c) (present; used by Y3 Lemma 3.4 / Theorem 3.5 and V3 Section 1 only); (SF*), (SF_tau), (b'), (Z0), (GM), (FD) and owners
  relative to L_N (present; used only by V4); the super-exponential decay of mu (present; used only by RS' through (RR)).

### 4.5 Verdict of the audit.  PROVED (modulo the cited refereed results).
For T_final every result in the dependency trees of Master Theorem II, Master Theorem III' and Theorem RS' has its hypotheses
satisfied.  Exactly two changes to the literal Round-7 designs are required: C1 (B_mu(l) instead of 8^{sigma(l)}) and C7 ((GM) only for
l >= 2, c_1 = 1).  No result in the trees uses the explosive design, lacunarity, or a feature T_final lacks.

## 5. The current master theorem for T_final
Notation: N >= 1, p_N the norm with I = {1..N} built with T_final, U_final; f in S_{p_N^*} with forced data (xi, q_0, a, w, F, z, zhat,
e, nu); Rec_N := {f : (f, g) in cl NA((c_0, p_N), l_2^2) for every g in C(f)}.  Rates, classes (R, G), kept/dropped carriers, shift
sources (U1)-(U3), (L1)-(L3), shift patterns pi(w), enlarged shift patterns kappa^sh(w) and clean sub-windows are those of the rate
scheme of T_final (V1 Part 2, V2 Part 3, V2-ref P3).
 (SH_w)  I_up(w) ∪ I_lo(w) = {} (every block has an upper and a lower shift source at w), or c_{pi(w)}(f) >= u(w).
 rho^sh  rho^sh(kappa^sh(w), f) := min{viol(delta, tau) : ||delta||_1 = 1} for the shift-extended system (R1)-(R7) of V2 Definition 3.2.
 (C*)    [F finite] there is l_0 such that for every level l >= l_0 and EVERY clean sub-window w of level l:
             I_up(w) ∪ I_lo(w) != {},   c_{pi(w)}(f) <= b(w),   rho^sh(kappa^sh(w), f) <= b(w).
 Infinite-F hypotheses (Z5-ref R1, V3, V3-ref): bad set B := {l in L_N : r_l = 0}, B_K, B_F, B_np := {l in B : k(l) strict non-peak},
 (W*), (H2), (H3-inf), (B_fin), (CS_B), (ND'_{B_np}) a|_F notin span{u_l|_F : l in B_np}, (RR_{U_{B_np}}) sum{mu_s U_{B_np}(s) : s in F,
 |a_s| < y U_{B_np}(s)} = O(y^{1+eps}) for some eps > 0, with U_{B_np}(s) := sum_{l in B_np} |u_l(s)|.

MASTER THEOREM.
 (i) [F finite; PROVED]  If for infinitely many levels some clean sub-window w satisfies (SH_w) or rho^sh(kappa^sh(w), f) >= u(w), then
     f in Rec_N.  Equivalently: f notin Rec_N implies (C*).  Independently of (C*): f in Rec_N if f is block-tame (cor:BTrecovered) or
     f in R_0 ∪ R_0^± ∪ R_S (thm:R0, thm:Bpm, thm:S).  Rows with z = eps_0 constant off F never satisfy (C*), hence are in Rec_N.
 (ii) [F infinite; PROVED]  f in Rec_N under any of:
     (RS')  (W*), (H2), (H3-inf), (B_fin), (ND'_{B_np}), (RR_{U_{B_np}})   [V3 Theorem RS + V3-ref Section 3];
     (R1)   (W*), (H2), (H3-inf), (B_fin), (CS_B)                         [Z5-ref Theorem R1];
     (Y3)   the super-critical support-swallowing class of Y3 Theorem 3.5, and the box-dominated class of Y3 Theorem 5.1
            [(BD) Bx <= C_a |a|, (SC_I), (W_M); any admissible T];
     (Z5)   signature room at infinite F (Z5 T6) and sign-mixed/cushion room (Z5 T7, with Z5-ref's fix).
     Per mate (not per row): V3 Theorem A (fixed d-neutral two-piece data with (RR_W), (ND'_{L_0})), Y3 Theorems 2.1, 6.1; (LSC-trunc)
     for all of these (V3 Corollary 4.2, Y3 6(b)).
 (iii) [RESIDUAL; PROVED as a logical statement]  If f notin Rec_N, then
     F finite: (C*) holds and f is not block-tame.  [Route sketched in V2 Theorem C6 (SKETCH), open sub-steps: C*-1 exact absorption of
       fine-peak residues on the coarse free coordinates; C*-2 (SC) at companions in configuration (i); C*-3 exactification of the block
       scalars theta_m, A_m; C*-4 a shift direction constant along the scales of a window when two or more blocks are shifted; C*-5 a
       joint completion/absorption fixed point.]
     F infinite: every criterion of (ii) fails; in particular at least one RS' hypothesis fails:
       (E1) (RR_{U_{B_np}}) fails — mu-thin supports (|a_s| below a power of mu_s on infinitely many active coordinates);
       (E2) (B_fin) fails — infinitely many bad carriers ((O4-box): bounded switching fails, the needed raise is scale-free);
       (E4) (ND'_{B_np}) fails, or (H3-inf) fails (a bad carrier at a degenerate peak with the swallowing sign, or a B_F carrier at a
            degenerate peak);
       (E5) (W*) or (H2) fails — the finite-F core at infinite F (V3 Theorem M_inf: reduction PROVED, transport of Master Theorems
            II/III' SKETCH; open rate: the VP' constants C_0(j) for carrier sets growing with the level need log C_0(j) = o(n(w_j))).
       (E3) (non-d-neutral fixed data at raised rows: (SC) at f_y) obstructs the per-mate Theorem A only; it is not a row class.
 (iv) [DENSITY; OPEN]  For p_N:  NA((c_0, p_N), l_2^2) dense  <=>  Lemma Z for T_final and N (thm:reductionZ; valid for T_final by
     Section 4)  <=>  Rec_N = S_{p_N^*}  <=>  every row of the residual classes of (iii) lies in Rec_N.  (C*), (E1), (E2), (E4), (E5) are
     open for every N, so density for p_N is OPEN.  For Martin's norm p (I = N) built with T_final, U_final: by lem:martintail, density for
     p follows from density for p_N for infinitely many N, since T_final and U_final do not depend on N (Lemma W).  The hypotheses in
     (i)-(iii) are N-independent in the sense needed: design, rate scheme, sub-windows and design constants are N-free; only the rate
     VALUES and f-constants depend on N (through f), with value 1 for objects involving absent carriers.  No row-wise statement transfers
     from p_N to p (lem:martintail transports density, an operator statement; V3 Remark 3.5(e), second clause, is FALSE, V3-ref F7).
     Density for p is OPEN.  Conditional form (PROVED): if for infinitely many N every first row of p_N in the residual classes of (iii)
     belongs to Rec_N, then NA((c_0, p), l_2^2) is dense for the norm p built with T_final, U_final.
Proof.  (i) By Section 4, every hypothesis of Master Theorem III' (V2-ref 4b) holds for T_final, so the first sentence holds.
Contrapositive: if f notin Rec_N, then at all levels l beyond some l_0 (>= l_f) every clean w has rho^sh < u(w) and not (SH_w).  At a
clean w, rho^sh and c_{pi(w)} are rate objects of level l, so they avoid (b(w), u(w)); hence rho^sh <= b(w), and not (SH_w) means
I_up ∪ I_lo != {} and c_{pi(w)} < u(w), so c_{pi(w)} <= b(w): this is (C*).  cor:BTrecovered is [any T]; thm:R0, thm:Bpm, thm:S are
[SLD] and hold by Lemma GW.  If z = eps_0 off F, Z4 Lemma 5.0 gives in every block non-degenerate peaks of both swallowing types with
margins >= q_0/4 (f-constants), which at every clean w of large level are robust sources (L2) and (U2); so I_up ∪ I_lo = {} and (SH_w)
holds at every such w (V1 M-II.3, V2-ref P5(i)).  (ii) Section 4.3 for RS'; R1, Y3 Theorem 3.5 and Z5 T6, T7 by Lemma GW; Y3 Theorem 5.1
for every admissible T.  (iii) Contrapositives of (i) and (ii); (E1), (E2), (E4), (E5) group the negations of the RS' hypotheses as in
V3-ref Section 7.  (iv) thm:reductionZ, prop:reduction (density <=> every (f, rho g) with g in C(f), rho < 1, is in cl NA), lem:martintail,
Lemma W.  QED

## 6. Status flags: what the master theorem rests on
 SKETCH dependencies on the critical paths of (i) and (ii): NONE.  The SKETCH items of Rounds 4-7 (Z1 Theorem M; Z4 steering under (FS);
   Y2 6.4 (weak peaks via the explosive design); the Y4 assembly (superseded by V1, PROVED); V2 near-coordinate conversion and Theorem C6;
   V2-ref (SC)-regularization route; V3 Theorem M_inf transport, (O4-box) 4.4, Remark 3.5(c),(d); V4 Remark 2.3(2)) occur only in the
   descriptions of the residual (iii).
 "PROVED by inspection" (refereed, weaker standard) on the critical paths: Lemma GW (window theorems on sub-windows; same meta-argument as
   V1 Theorem 1'(d)); Z3 Lemma U / Y2 Lemma U' / V1 Theorem E'' (budget lemmas re-read with banked and pulled supports); Theorem RS' items
   (I1)-(I3) (V3-ref).
 Single-referee items (proved in a referee report, not re-refereed) on the critical paths: V1-ref p0-p5 (precisions); V2-ref P2, P3, P7
   and Master Theorem III' (logic re-verified, 4.4(c)); V3-ref Lemma VP' (re-verified, 4.4(b)) and the (H3-inf) strengthening of RS' (if
   only double-refereed statements are wanted, use RS with (H3') "no bad carrier at a degenerate peak", V3's refereed statement with the
   (ND') fix); Y4-ref C.1-C.7 (re-verified and re-proved by V1, refereed).
 New defects found in this audit, both FIXED in T_final: C1 (B_mu), C7 ((GM) for l >= 2).  Neither changes any conclusion of Rounds 5-7.
 FALSE statements recalled (must not be used in the write-up): V3 Remark 3.5(e), second clause (row-wise transfer of RS to p); V4
   Proposition 2.4 as stated (corrected by V4-ref R2); V1's gloss on (B) (V1-ref); V2 Cor. C3.1(c) beyond constant-sign maximal contact
   (V2-ref P5).

## 7. Numerics (evidence only; r8/U4_work/)
 tu_mu_check.py (C1): V1 Lemma TU (pulls + private banks + explicit scalar fixed point) in the finite model of V1-ref tu_check4.py with
   base entries s_j = 2^{-beta j^2}, beta in [0.002, 0.006] (finite analogue of mu_s), signature weights 2^{-alpha s}, bounded gaps; tuning
   sizes proportional to min_l s_{j'}^2 v(j').  587 tests, 0 failures (no divergence, all bank masses > 0, increments >= eta/2); exactness
   |val^# - val^(2) - x| <= 9.3e-16; other carriers move by <= 1.6e3 eta^2 with a constant independent of eta over four decades (second
   order); |Phi'| <= 2.6e-3 at the fixed point; bank mass x min(s'^2 v')/eta in [O(1), 13.6]: bank masses scale like eta/(s'^2 v'), the
   quantity B_mu(l) controls.  (613 configurations skipped: no pull coordinate in range in the truncated model.)
 rr_check.py (C1(v)): local exponent kappa(y) = log M^W(y)/log y for W = 2^{-s}, |a_s| = 2^{-(1+b)s} on a bounded-gap set, at y = 2^{-200},
   2^{-400}, 2^{-800}.  Base 2^{-s}: kappa ~ 2/b (4.0, 2.0, 1.33, 1.0, 0.67, 0.40 for b = 0.5, 1, 1.5, 2, 3, 5): (RR) fails for b >= 2.
   Base 2^{-s^2-1}: kappa grows without bound (b = 5: 9, 17, 33): (RR) holds for all b.

## 8. Recommendations for the write-up
 1. Present ONE operator: Section 1 of these notes (T_final, U_final), with the R6 order and the two fixes C1, C7; state Theorem 2.2
    (admissibility and Lemma B) and Lemma W first, then the feature list (F1)-(F11).
 2. State the window meta-lemma GW once and use "any sub-window of level l" throughout; record that every window theorem uses only
    (i)-(iv) of GW (this replaces all "survival" lists of Rounds 5-7).
 3. Replace V1's Master Theorem II by Master Theorem III' (no (VR_w)) and state the residual (C*) in the rate-object form of 5.
 4. State Theorem RS' as a theorem about p_N (per row); never as a statement about Martin's p.  For p, only the conditional form (iv).
 5. Optional simplifications: (FD) can be dropped (it serves only the negative V4 Proposition 5.8); V4's (SF*), (SF_tau), (b'), (Z0), (GM)
    are needed only for V4's statements (Construction SA, Proposition 5.3, Theorem 5.6, Proposition R5), i.e. for the realizability of
    (C) and for the exact-data route, not for the master theorem.  Allowedness (c) is needed only for Y3's Theorem 3.5.
 6. Keep the labels of Section 6: no SKETCH on the critical path; the inspection-standard and single-referee items should be written out
    in full in the paper (Lemma GW, Lemma U with banked/pulled supports, RS' items I1-I3, VP', III').

## 9. What remains open (unchanged by the audit)
 Lemma Z and density of NA((c_0, p_N), l_2^2) for T_final and every N; density of NA((c_0, p), l_2^2) for Martin's p built with T_final;
 hence Johnson-Wolfe's question for these spaces.  Precisely: (C*) at finite F (with sub-steps C*-1..C*-5), and (E1), (E2), (E4), (E5) at
 infinite F (with (E3) for the per-mate route).  Nothing found in this audit points to a counterexample; the audit found no error that
 changes a conclusion of Rounds 5-7, only two design-bookkeeping defects (C1, C7), both fixed.
