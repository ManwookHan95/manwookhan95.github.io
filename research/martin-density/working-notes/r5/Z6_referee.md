# Referee report on Z6 (Round 5): stress test (maximal contact), numerics, and the design route D''

Refereed: r5/Z6_notes.md (with Z6_part0..8.md, scripts r5/Z6_work/*.py) against the note paper/martin_density_note.tex
(Sections 1, 7, 8; Lemma martintail, Theorem engineered, Corollaries D1, BTrecovered, all of Section 8), the Round-4/5
reports used by Z6 (Z4 notes and referee, Z3 referee).  Referee part files: r5/Z6_ref_part0..5.md; assembled proofs of all
fixes and additions: r5/Z6_ref_notes.md; scripts and outputs: r5/Z6_ref_work/.

## Overall verdict
The structural results of Z6 are CORRECT: the d-coefficient formula (2.1), shift pinning by a pair of swallowed peaks (2.2),
d-neutrality of exact two-piece data in doubly swallowed blocks (2.3), same-sign transience (2.4), Lemma F and Corollary 4.2
(one sign typo), Theorem C, combinatorial Hoffman constants (5.2), Proposition P, Corollary V.1, the gap-rate remark.  Every one
was re-derived; Proposition P and the shift trick were also checked numerically, and Z6's experiment R4 was re-run and
reproduced exactly.  The design part has FIXABLE GAPS: D'' depends on N (it must not, for Lemma martintail); one estimate of
signature masses (sum 1/m_l <= C_f sum 1/m^des) is false when signature sets meet F; "D'' windows dominate those of SLD_G" is
false in general; and the growth condition (W_U) of Theorem U squares Lambda*_f, which at maximal contact is comparable to
Lambda°, so the advertised maximal-contact consequences (including "the candidate is recovered for D'' unless K_nn ...") do not
follow from Theorem U as stated.  All four are repaired (design D''', Theorem U' with the good-only room product Lambda_g and
linear bookkeeping).  The sign-alternating claim 5.5 is misstated (fixed).  No counterexample is claimed or indicated.
Lemma Z and density remain OPEN for SLD, for D''' and for every admissible T.

## Verdicts
| claim | Z6 label | verdict | issue / fix |
|---|---|---|---|
| 2.1 d-coefficient | PROVED | correct | — |
| 2.2 shift pinning | PROVED | correct | non-degeneracy of the anti-sign peak k_1 not needed; the pair's constant t/(lambda mu) is a fixed margin (f-constant) |
| 2.3 doubly swallowed blocks | PROVED | correct | re-derived (allowedness (b) tail estimate); same content as Z4 Prop 5.1 / Z4-referee finding 9 |
| 2.4 same-sign transience | PROVED | correct | elementary from (didentity); numerics show the 1/q constant is essentially attained (R4 re-run) |
| Lemma F, Cor 4.2 | PROVED | correct | 4.2(b) should read g on A = eps_l theta*_l v_l; A may be empty |
| Theorem C | PROVED | correct (fixable formal gap) | shift trick verified by hand and numerically; Lemma onesidedtransfer must be restated with "inward-only" coordinates (Lemma 2.1 of ref notes, proved) |
| Design D'' | PROVED | correct with fixable gaps | (i) 8N factor makes D'' N-dependent: replace by 1/Phi_l (|q_l| >= Phi_l/2, proved); (ii) m^des must remove [1,l] (else false for S_l meeting F); (iii) "dominates SLD_G" false: put (l 2^{l^3} Lambda° G*)^5 into Xi. Fixed design D''' |
| Combinatorial Hoffman constants | PROVED | correct | constant independent of right-hand sides (Hoffman 1952); patterns over all subsets of [1,l]: N-free |
| Theorem U | PROVED | correct with fixable gaps | D''-gaps above; (W_U) squares Lambda*_f, ≍ Lambda° at maximal contact, so "maximal contact allowed" needs Lambda° = o(l 2^{l^3}) (not imposed). Fix: Theorem U' with Lambda_g (good carriers only; modswallow(a) uses only good indices) and linear bookkeeping |
| Gaps as a rate | PROVED | correct | constraints on c_flat are upper bounds, t_1 monotone; agrees with Z4 Lemma 6.1 |
| Sign-alternating signatures | PROVED | correct with a misstatement | survival of Section 8 verified; claim needs r_l > 0 on the finitely many exceptional S_l; relabelling only |
| Proposition P | PROVED | correct | Farkas; monotonicity by extension by zero; 1232 random rigid instances checked |
| Theorem V | PROVED | correct (precision in (b)) | (b): K_A over the active-set cones of Z4, or inactive carriers in the bracket; at maximal contact (a) is vacuous in compensated blocks (ref Prop R1) |
| Corollary V.1 | PROVED | correct | — |
| Candidate data | SKETCH | plausible, inconsistent detail | F = {j0}, z ≡ 1 has NO free parameter; nested construction needs abs(F) >= 2; (C2) does not violate (W_U) |
| Single-module mates | SKETCH | plausible | − side beyond the radius needs base/block rebalancing (levels unequal), routine |
| Module sums | SKETCH | plausible in its (non-switching) regime | covers only c_i^2 <= eps gamma_i lambda_i; switching sums are HEURISTIC (as Z6 says) |
| Candidate under D'' | PROVED | correct after fix | follows from Theorem U' (Cor 3.4' of ref notes): recovered unless liminf K_nn/(l 2^{l^3} Lambda°) > 0; not from (W_U) as written |

## Main findings (details and proofs in Z6_ref_notes.md)
1. N-dependence of D'' (fix proved): |q_l| >= Phi_l/2 for peaks and near-threshold non-peaks (M >= 1/2, C_m <= 2^{-m}), so the
   N-free factor 1/Phi_l replaces 8N 2^{m+k}/c_l.
2. Signature masses (fix proved): with m^nat_l(l) := ||v_l 1_{S_l \ ([1,l] ∪ T(l))}||_1 one has m_l(l*) >= m^nat_l(l*) for l* >= max F;
   Z6's comparison with ||v_l 1_{S_l \ T(l)}||_1 fails when F contains the leading point of S_l \ T(l*).
3. Window domination: SLD_G's n^w = (l 2^{l^3} Lambda° G*)^6 is not dominated by D'''s l 2^{l^3} Lambda° Xi when delta°_l is tiny;
   D''' inserts (l 2^{l^3} Lambda° G*)^5 G*^4 explicitly.
4. (W_U) and maximal contact: Theorem U uses only Lemma modswallow(a), whose unrolling involves good indices only, so Lambda*_f
   can be replaced by Lambda_g (= 1 at maximal contact); the violation total is linear in each rate.  Theorem U':
   liminf Lambda_g (1 + K_P + K_R)/(l 2^{l^3} Lambda°) = 0 suffices, with "uncompensated" generalized to "rigid" blocks
   (all q != 0 bad carriers d-rigid; relative Farkas rate K_R, <= C_f(1 + K_nn) in one-signed blocks).
5. New (Prop R1, proved under the harmless design choice that the targets contain a dense set of nonnegative vectors): at
   maximal contact, a block with a resonant q < 0 swallowed strict non-peak has ALL its swallowing-type peaks non-rigid.  So
   Theorem V(a) never applies in compensated blocks at maximal contact; every positive peak's relative margin there is a rate,
   and a degenerate positive peak there is in the open case (d).  This sharpens Z6 8.2: at maximal contact the hard blocks are
   exactly those carrying a negative (q < 0) zero-cost resource.
6. Theorem C, 2.4 and Lemma 2.1: the "inward-only" one-sided expansion (no gap needed for coordinates moving inward on their
   side) is correct; Lemma onesidedtransfer should be restated accordingly (done).

## Attacks attempted (none broke a PROVED claim beyond the fixes above)
weak* vs norm (decompositions exist at every scale; compactness only qualitative); uniformity in t, window and number of active
carriers (all constants are f-constants times design quantities at level l*; H_comb over all subsets of [1,l*]); Hoffman constants
(right-hand-side independent; feasibility via 0); non-attained infima (Farkas/LP minima attained); signs (peakshift, suplevel(c),(f),
phicalc, split lemma, Farkas inequality); near-contacts vs contacts (gamma_T, Lambda_g, budget gloss); c_0 vs l_infty (z in l_infty,
engineered approximants truncate); finite vs infinite B, P, K (box rows; fine carriers 6t^5); I finite and N-independence (found
gap 1); hidden assumptions on T (only (T-a)-(T-d), (P1)-(P3), allowedness; 5.5 needs s_1 = s_0 + 1, a design choice); quantifier
order (window data built from g, rho; engineered f' inside Corollary D1 after averaging); gaps between windows: in D''/D''' the
factor 1/c_{l+1} in Xi(l+1) forces T_hi(l+1) < T_lo(l), so the windows are NOT contiguous, but every proof uses only dyadic
scales inside the chosen windows (and 4.2(b) only needs some sequence t_n -> 0, which can be taken in windows): harmless.

## Single most valuable idea
The d-rigidity dichotomy (2.4 + Proposition P + Corollary V.1): at a window level, a swallowed carrier on which every zero-cost,
exactly d-neutral direction vanishes is pinned at O(t) by an LP (Farkas) certificate; in one-signed blocks the certificate is the
d-row itself, of size ~ 1/Phi_l, a DESIGN quantity that a ladder with windows lengthened by the reciprocal weights absorbs.  Hence
margins and degeneracy of swallowing-type peaks matter only for NON-rigid peaks, which exist only alongside non-rigid q < 0
swallowed non-peaks (and, at maximal contact, always do then: ref Prop R1).

## What remains open
Lemma Z (equivalently density for p_N) is open for SLD, for D''' and for every admissible T.  For D''' and F finite the open
pairs (f,g) (g not window-pinned) have f outside R_0^pm ∪ R_S ∪ R_BT ∪ R_C ∪ R_U' ∪ R_SBinf, i.e. at least one of:
(r) rates beyond the ladder: Lambda_g (rooms of good signature sets, incl. approximate swallowing (O1)(i)), K_P (relative margins
of non-rigid positive peaks in compensated blocks -- at maximal contact all positive peaks of such blocks), K_R (relative Farkas
constants; in one-signed blocks the relative d-coefficients K_nn of nearly neutral swallowed non-peaks; Conjecture G would remove
it), gaps gamma_B(l), rooms gamma_T; (d) degenerate non-rigid swallowing-type peaks, which occur exactly in blocks with a non-rigid
q < 0 swallowed strict non-peak (needs peak-carrying engineering, Z4 part 8 / Z4-referee 9.3, open at maximal contact);
(m) mixed blocks neither compensated nor rigid (f-dependent d-row Hoffman constants); (h) failure of (H2') / (H2'');
(e) failure of (E1)/(E2); (O4) infinite F.
