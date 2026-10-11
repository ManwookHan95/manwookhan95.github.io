# G1 part 1 (Round 14): a cushioned, face-wise Hoffman lemma

Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  Scripts: r14/G1_work/.

## 0. Where exactness on Z_kappa is used (reading of the chain)
The realized active ratios r'' of Step A must lie on Z_kappa (all TINY rate objects vanish) for exactly one reason
(J1.13, Lemma CM^tr item (iii), Lemma II-classes, Prop II-ray(b)): the coarse decomposition data X(t) = (Delta'_dec(t),
gamma_dec(t)) of g at f (after zeroing the inactive components of the class) violate the rows of the class cone
Gamma^#(kappa, a; r) at the realized ratios by at most K t, and they are projected onto that cone; Lemma H (V2) bounds the
Hoffman constant by (norm)^{n-1}/(least NONZERO minor), so tiny nonzero minors would give constants ~ 1/b.  Everything
else downstream uses ratios only through statuses and move sizes (J1.13 proof, J1-ref B.5).

Units (needed later).  The coarse data are bounded uniformly in the scale: |X(t)| <= K_X := C_f Des(L)^C for t in the
window (coarse omega^+- components are bounded by the Gamma_w-seminorm through 1/Phi_l <= D(L); the switching amplitude
gamma_l = lambda_l(Delta omega(l) - Delta_m w(k(l))) and the shift |Delta'| <= C_Delta are bounded; Prop II-ray(c):
coefficients <= A_max <= K).  Violations are <= K t (Prop II-ray(a)).

## 1. The lemma
Setting.  Rows a_1, ..., a_p in R^n (row vectors), |a_i|_2 <= 1, index set [p] = E u I_s u I_c (equality rows, STRICT
inequality rows, CUSHIONED inequality rows); S := E u I_s (the strict rows), I := I_s u I_c.  For beta = (beta_i)_{i in I_c}
>= 0 put
   C := {x : a_i x = 0 (i in E), a_i x >= 0 (i in I)},
   P_beta := {x : a_i x = 0 (i in E), a_i x >= 0 (i in I_s), a_i x >= -beta_i (i in I_c)}   (so C = P_0).
For x in R^n: slack s_i := a_i x (i in I), violation V(x) := max( max_E |a_i x|, max_I (a_i x)_- ).
For a row set R: A_R its |R| x n matrix; vol(A_R) := det(A_R A_R^T)^{1/2} = (sum_K det(A_{R,K})^2)^{1/2} (Cauchy-Binet,
K over |R|-subsets of columns).  R is ROBUST at level u if some |R| x |R| minor of A_R has modulus >= u (the empty set
is robust, vol := 1).
Facts used (elementary, PROVED in V2 Lemma H and by Cauchy-Binet):
 (F1) sigma_min(A_R) >= vol(A_R)/||A_R||_2^{|R|-1} >= vol(A_R)/|R|^{(|R|-1)/2}   (||A_R||_2 <= ||A_R||_F <= |R|^{1/2});
 (F2) if A_R has independent rows and i notin R: dist_2(a_i, rowspace(A_R)) = vol(A_{R u {i}})/vol(A_R)
      (Gram determinant: vol^2 of R u {i} = vol^2 of R times the squared distance of a_i to the span).

Hypotheses, for numbers 0 <= mu < u <= 1 and a row set N (the "rows met by the data", defined in the lemma):
 (MD_N) minor dichotomy: every square minor of A_N has modulus <= mu or >= u;
 (SE_N) strict exactness: every square minor of A_{N cap S} is 0 or has modulus >= u.

LEMMA CH (cushioned face-wise Hoffman lemma).  PROVED.
Let x in R^n, V := V(x), Lambda := p^{p/2}/u + 1, and
   N := E u {i in I : s_i < Lambda^p V}            ("rows met by the data at the scale of the violation").
Assume (MD_N) and (SE_N).  Put H := p^{p/2} Lambda^p/u and eta := 2^{n/2} mu/u.  Then there is x' in R^n with
 (i)   |x' - x|_2 <= H V;
 (ii)  a_i x' = 0 for every i in E, and a_i x' >= 0 for every i in I_s   (strict rows hold EXACTLY);
 (iii) a_i x' >= -eta |x'|_2 for every i in I_c (and a_i x' >= 0 for i in I_c \ N);
 (iv)  in particular x' in P_beta whenever beta_i >= eta (|x|_2 + H V) for all i in I_c cap N; and x' in C itself if every
       cushioned row of N is in the robust span chosen below or has defect d_i with d_i x' >= 0 (see (v));
 (v)   (sign form) for i in I_c cap N one has a_i x' = d_i x' with a vector d_i of norm <= eta orthogonal to the span of the
       rows of a robust set B subset N; so only the SIGN of the defect along x' matters when beta_i = 0.
Only minors of rows in N are used: rows with slack >= Lambda^p V at x are irrelevant ("face-wise"), and minors that contain
a cushioned row are needed only to be small (<= mu), not zero.

Proof.  If V = 0 take x' = x.  Let V > 0.
Step 1 (slack pigeonhole).  Put rho_k := Lambda^k V (k = 0, ..., p).  The at most |I| <= p numbers s_i (i in I) cannot meet
all p+1 intervals [rho_k, rho_{k+1}); fix k with no s_i in [rho_k, rho_{k+1}) and put rho := rho_k, N_k := E u {i in I :
s_i < rho} (subset of N, since rho <= rho_p).  Every i in I \ N_k has s_i >= Lambda rho.
Step 2 (strict basis).  Let q := rank A_{S cap N_k}.  If q >= 1 there are B_s subset S cap N_k with |B_s| = q and a q x q
minor of A_{B_s} that is nonzero, hence of modulus >= u by (SE_N); then rank A_{B_s} = q = rank A_{S cap N_k}, so every
a_i, i in S cap N_k, lies in rowspace(A_{B_s}).  (If q = 0 put B_s := empty.)
Step 3 (robust extension).  Among the robust sets B with B_s subset B subset N_k choose one of maximal cardinality (B_s is
such a set).  vol(A_B) >= u, so A_B has independent rows and, by (F1), sigma_min(A_B) >= u/p^{(p-1)/2}.  For i in N_k \ B,
the set B u {i} is not robust (maximality), so every (|B|+1)-minor of A_{B u {i}} has modulus < u, hence <= mu by (MD_N);
there are at most 2^n of them, so vol(A_{B u {i}}) <= 2^{n/2} mu and, by (F2), dist(a_i, rowspace A_B) <= 2^{n/2} mu/u = eta.
Write a_i = pi_i + d_i with pi_i in rowspace(A_B), |d_i| <= eta (for i in B: d_i = 0).
Step 4 (projection onto the face of B).  x' := x - A_B^T (A_B A_B^T)^{-1} A_B x, the Euclidean projection of x onto
ker A_B.  For i in B: |a_i x| <= rho (equality rows: <= V <= rho; inequality rows of N_k: -V <= s_i < rho).  Hence
|x' - x| <= |A_B x|_2/sigma_min(A_B) <= p^{1/2} rho p^{(p-1)/2}/u = p^{p/2} rho/u <= H V.
Step 5 (verification).  A_B x' = 0, so for every i in N_k: a_i x' = pi_i x' + d_i x' = d_i x'.
 - i in S cap N_k: a_i in rowspace(A_{B_s}) subset rowspace(A_B), so d_i = 0 and a_i x' = 0.  All equality rows are in N_k.
 - i in I_c cap N_k: a_i x' = d_i x' >= -eta |x'|.
 - i in I \ N_k: a_i x' >= s_i - |x' - x| >= Lambda rho - p^{p/2} rho/u >= rho > 0.
This gives (i)-(iii) and (v); (iv) follows from |x'| <= |x| + H V.  QED

Remarks.  (a) The constant H depends only on p and u (no tiny quantity); eta is linear in the largest tiny minor mu.
(b) If (MD_N) holds with mu = 0 (all minors of the met rows are 0 or >= u) the lemma is a local form of Lemma H with
cushions not needed.  (c) Equality rows can never be cushioned in this argument: a tiny nonzero minor among met STRICT rows
genuinely destroys the face (two-ray example of V2 2.1: D tau = (0, delta), dist >= 2/delta).  So (SE_N) cannot be
weakened to (MD_N) for strict rows: exactness is necessary for strict rows (PROVED by that example).  (d) For cushioned
rows the tolerance condition is sharp up to constants: in the 2 x 2 example of Section 3 below, with the wrong sign of the
defect the data are at distance ~ |x| from C, and x' violates the cushioned row by exactly |d_i x'|.

## 2. Parametric form (the shape in which the transplant uses it)
Let A(r) be a matrix whose rows depend Lipschitz-continuously on a parameter r (constant Lip), split into E, I_s, I_c as
above.  Let X be a data point with violation V_0 of the rows of A(r_0) for some r_0, and let r^# be another parameter.
COROLLARY CH.1.  PROVED.  Suppose that at r^# (MD_N) holds with (mu, u) and (SE_N) holds, where N is computed at r^# with
V := V_0 + Lip |r^# - r_0| |X|.  Then there is X^# with all strict rows of A(r^#) exact, cushioned rows >= -eta|X^#|, and
|X^# - X| <= H (V_0 + Lip |r^# - r_0| |X|).
Proof.  The violation of X at r^# is <= V_0 + Lip|r^# - r_0||X|; apply Lemma CH at r^#.  QED
So the realized parameter needs: exactness of the met strict minors, smallness (<= mu) of the met minors containing a
cushioned row, robustness (>= u) of the others; no exactness of any minor that contains a cushioned row.
