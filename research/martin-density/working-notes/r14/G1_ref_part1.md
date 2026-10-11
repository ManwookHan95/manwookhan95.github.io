# G1-ref part 1: Lemma CH, Remark CH(c), Corollary CH.1

Refereed: r14/G1_notes.md Section 2 (= G1_part1.md).  Scripts: r14/G1_ref_work/.

## 1.1 Lemma CH -- re-derivation (verdict: CORRECT; precisions P-CH1, P-CH2)
Setting as in G1: rows |a_i| <= 1 in R^n, [p] = E u I_s u I_c, S = E u I_s, I = I_s u I_c, slacks s_i = a_i x, violation V.
Step 1 (pigeonhole).  rho_k = Lambda^k V, k = 0..p; the <= p inequality slacks miss one of the p+1 half-open intervals
[rho_k, rho_{k+1}).  With rho := rho_k and N_k := E u {i in I : s_i < rho}: N_k subset N (rho <= Lambda^p V) and every i in
I \ N_k has s_i >= Lambda rho.  Correct.  (Note s_i >= -V >= -rho for i in I.)
Step 2.  q = rank A_{S cap N_k}; a q x q nonzero minor of A_{B_s} is a minor of A_{N cap S}, hence >= u by (SE_N).  Correct.
Step 3.  Robust sets have independent rows (a nonzero maximal minor), so |B| <= n.  For i in N_k \ B either a_i is in the row
space of A_B, or B u {i} has rank |B|+1 and, not being robust (maximality of |B| among robust supersets of B_s), has all
(|B|+1)-minors < u, hence <= mu by (MD_N) (B u {i} subset N_k subset N).  There are C(n, |B|+1) <= 2^n of them; by
Cauchy-Binet vol(A_{B u {i}}) <= 2^{n/2} mu and by the Gram identity dist(a_i, row A_B) = vol(A_{B u {i}})/vol(A_B) <= eta.
For i in S cap N_k, a_i lies in row A_{B_s}, so d_i = 0.  Correct.
Step 4.  sigma_min(A_B) = vol(A_B)/(product of the other |B|-1 singular values) >= u/|B|^{(|B|-1)/2}; |A_B x|_2 <= |B|^{1/2} rho;
hence |x' - x| <= |B|^{|B|/2} rho/u.  Since |B| <= n this is <= n^{n/2} rho/u <= n^{n/2} Lambda^p V/u <= H V.  Correct.
Step 5.  A_B x' = 0 gives a_i x' = d_i x' on N_k; i in I \ N_k: a_i x' >= s_i - |x' - x| >= Lambda rho - p^{p/2} rho/u = rho > 0.
Correct.

P-CH1 (statement (iv)/(v)).  The sign form a_i x' = d_i x' holds for i in I_c cap N_k (the met rows at the selected level), not
for all i in I_c cap N; for i in I_c cap (N \ N_k) one has a_i x' >= rho > 0 instead.  Harmless.
P-CH2 (constants).  The proof gives the sharper |x' - x| <= n^{n/2} Lambda^p V/u and Lambda may be taken n^{n/2}/u + 1 (with
n <= 2L active variables); the factor Lambda^p (p = number of ROWS) comes only from the pigeonhole and is genuinely used by
the construction (numerics: |x' - x|/V up to 1.0e6 at u = 1e-3, p <= 7, when the gap is found at k >= 1).  This matters for
the window count (see part 2, P-W).

Numerics (ref_ch_check.py/.out, independent implementation, exhaustive maximal robust extension): 600 random instances,
n in {3,4,5}, p <= 7, strict rows with exact dependencies, cushioned rows with planted tiny defects of random sign (mu in
[1e-11, 1e-8]), (MD)/(SE) verified by enumerating all minors: strict rows exact 600/600, cushioned rows >= -eta|x'| 600/600,
|x' - x| <= H V 600/600, sharper bound |B|^{|B|/2} rho/u 600/600, |B| <= n 600/600; |x' - x|/V median 1.8, max 1.0e6.
(One NaN instance of a first run came from a degenerate random construction, excluded.)  G1's ch_lemma_check / ch_debug2
outputs re-read: consistent.

## 1.2 Remark CH(c) (necessity for strict rows) -- CORRECT
Two equality rows a_1 = e_1, a_2 = (e_1 + delta e_2)/|.|: the exact set is {x_1 = x_2 = 0}; the data x = e_2 have violation
V = delta/|.| ~ delta and distance 1 = V/delta from the exact set.  So with a tiny NONZERO strict minor any point with strict
rows exact is at distance ~ V/delta, i.e. no design-controlled constant: (SE_N) cannot be weakened to (MD_N) on strict rows.
(MD_N) holds there with mu = delta; Lemma CH's conclusion (ii) with |x'-x| <= HV is impossible.  This is V2's two-ray example.
Remark CH(d) (sharpness for cushioned rows): numerics only; consistent with Lemma CH (v).

## 1.3 Corollary CH.1 -- CORRECT (with P-CH3)
At r^#: |a_i(r^#)X - a_i(r_0)X| <= Lip |r^# - r_0| |X|, so the violation of X at r^# is <= V := V_0 + Lip|r^# - r_0||X|.
Hypotheses on a superset N' of the true met set (computed with the larger V) imply them on the true met set, since minors of
A_N are minors of A_{N'}.  P-CH3: Lemma CH needs |a_i| <= 1, so the rows are normalized at r^#; dividing a row by its norm
nu_i divides every minor containing it by nu_i, so the robust threshold of the NORMALIZED matrix is u/prod nu_i (product over
at most n rows) -- see part 2, P-N.  For the class cone with the natural units below this costs a factor <= (8L)^{L} <=
Des(L)^{1/2}.

## 1.4 Assessment
Lemma CH is a correct, clean piece of linear algebra: a Hoffman-type projection that keeps the strict rows exact and leaves
cushioned rows violated by at most (2^{n/2} mu/u)|x'|, with a constant depending on p, n, u only.  It does what the Round-13
reports asked for ("a face-wise Hoffman bound insensitive to tiny minors not met by the data"), in the stronger form
"insensitive to tiny minors containing a cushioned row".  Its constant is much worse than V2 Lemma H's (Lambda^p instead of
Des^C/u), which has to be paid in the window count (part 2).
