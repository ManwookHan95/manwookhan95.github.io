# X1-ref part 4 — Master Theorem IV^tr, Corollaries IV^tr.1, IV^tr.2, residual list

## 1. Master Theorem IV^tr.  Verdict: CORRECT (modulo U1-ref's refereed assembly of Master Theorem IV' and the fixes of parts 1-3).
I re-read U1-ref's proof of Master Theorem IV' (U1_ref_notes 8) step by step.  (KN_{w,a}) enters exactly at: (1a) Proposition KN
(exactification with statuses); "Statuses: Proposition KN(b) plus inward pushes; kinds [2] and [3] (Section 4.1)"; "(SC) ... U1 Lemma 4.3
(coarse statuses from Proposition KN)".  Lemma 4.3 needs only POSITIVE gaps of the coarse strict non-peaks (a threshold s_0(f^#) below which
they do not contribute to Scr), which KN^tr gives ((M/2) mu in (T)-blocks, c_f eta' D M in (KN)-blocks, eta' M in (U)-blocks).  Section 4.1's
(X4) is used in U1 Prop. 2.2(a) (data violate the row by <= K t) and (e)/(c) (points and increments of the cone are kind [3]): (X4^0) has
both properties (part 2, Section 2; increments: vs Domega(incr) >= -|Delta'(incr)| (rho^# - rho^0), and Delta'(t), Delta'(incr) have the same
sign (U1-ref (p-d)), so the bound for the sum is C_f C D^2 c_{L+1}^2 again).  U1 Lemma 4.6 (true versus reference shift): the kind-[3] bound
with the TRUE shift Delta''(t) at f^# needs lambda(|Delta'' - Delta'| + |Delta'| |rho^# - rho^0|) <= 3 lambda gap^#/t, i.e. C_f Design c_{L+1} t +
C c_{L+1}^2 << M mu: true by S-0 (part 3).  The window constants (Hoffman, A_max, D_cls) contain no 1/gap^# (kind [3] has no gap lower
bound; c_flat uses the kind-[2] threshold gamma(w) = min M u/4 only): checked against Y1 Prop. 5.2(iii) and V1 TR(iii).  Everything else is
U1-ref's assembly, valid for T^tr by Lemma W'(iv) (with W3).
Under option (b) the exception (carrier 1 in N_T) stands for N >= m(1); with m(1) = 2 it is void for N = 1 (part 3, W2).

## 2. Corollary IV^tr.1 (N = 1).  Verdict: CORRECT (modulo the same tools), for T^tr(a); and, with the fix W2 (m(1) = 2), for an operator
T^tr(b) that is admissible in the note's sense.
With one block every activity class is one-signed (A = {1}) or has no active shift (A = {}); clean sub-windows exist at every main stage
(pigeonhole with the enlarged rate scheme); some class carries >= n(w)/D_cls(w) scales (U1 2.3); the hypothesis of IV^tr holds at every main
stage, for every g in C(f) and rho < 1.  So every F-finite first row of p_1 is in Rec(p_1).
Status of the evidence: U1's assembly has been refereed once (U1-ref), with several repairs; Theorem E^SC / E^>= (V2), E'' (V1) twice-refereed
chains; Proposition KN^tr is new (this report).  "Finite-F Lemma Z for p_1" is therefore PROVED at the level of rigour of the refereed
programme, not independently of it.  Lemma Z for p_1 (infinite F) and density for p_1 remain OPEN.

## 3. Corollary IV^tr.2 (every N; conditional on X2).  Verdict: SKETCH (as labelled); plausible.
X2's Theorem C_mix (unrefereed) uses (KN) through U1-ref's Proposition KN and quantitatively through gap_min >= c_f T^4/(L Design) inside a
window constant K_w that is a polynomial in 1/gap_min (X2 4.2; also x_0 >= c_f gap_min Phi_min(L)).  With KN^tr, gap_min >= (M/2) c_kappa
(T^4/(3 L Design))^{beta_kappa}: K_w <= T^{-C' beta} with beta <= Design(L) (a level constant, not absolute).  X2's comparison (S2c) uses
(W_exp) c_{l+1} <= exp(-1/T_lo(l, M(l))), which dominates T^{C'' beta} because 1/T >> C'' Design(L) log(1/T) (T_lo <= 2^{-Q(w)}, Q(w) >=
Design(L)).  So the substitution is consistent; whether X2's proofs are correct is X2's referee's task.  Under option (b) the carrier-1
exception remains for N >= m(1).

## 4. What remains open (after X1 and this report), design T^tr, finite block set I = {1..N}
(1) Option (b), N >= m(1): rows whose weight-one carrier is an active near-threshold carrier of a (T)-block at clean sub-windows of almost all
    main stages (forces rho_1(f) = 1 exactly) and whose pattern has a coincidence on the slice Phi_1 = 2^{-m(1)-1}.  A slice version of
    Lemma NLM holds whenever 2^{-m(1)-1} is a regular value of psi_1 on every stratum (then CV of the slice has dimension < |N_T| - 1);
    whether the critical values of psi_1 can be identically equal to this rational number as functions of the transcendental parameters is
    OPEN.
(2) Mixed activity classes for N >= 2: X2's Theorem C_mix (to be refereed) + Corollary IV^tr.2.
(3) Infinite base support: (E1)-(E5) (ADDENDUM 7), U2's items, and status coherence at infinite F (patterns finite per level, so Lemmas F,
    NLM, GEN, QC should transfer; not checked).
(4) Martin's p: needs Lemma Z at infinite F for infinitely many N (lem:martintail); row-wise statements do not transfer.
Lemma Z and density of NA((c_0, p_N), l_2^2) (every N) and of NA((c_0, p), l_2^2): OPEN.  No counterexample is claimed by X1 or here; nothing
found points to one.
