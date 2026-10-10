# V4 referee, part 4: Sections 9-12 (rigidity of exact data, Theorem 5.6, dead zones, sequential projection, structure claim)

## 4.1 Lemma 4.1' and Proposition 4.2' (exact data force owner alignment).  CORRECT (with (G1) for p_N).
Lemma 4.1' re-derived in all three cases: (i) ratio <= (4/3)2^{-10} 2^{4 - min S_o} <= 2^{-5}; (ii) first later carrier at j has
c <= tau_o 2^{-2j} c_o delta_o/2 by (b'), later sum of lambda <= (1/3) tau_o 2^{-2j} c_o delta_o, times 4/3; leading >= (4/5) tau_o C_1 2^{-m-k} c_o delta_o 2^{-j};
ratio <= (5/9) 2^{m+k-j} < 2^{-5}; (iii) (SF_tau) gives ratio <= 2^{-9}.  No later carrier has j in its signature set (allowedness (a) /
disjointness).  Prop. 4.2' re-derived: a K_omega-carrier at j notin E must have j in its signature set, hence be the owner; so the
hypothesis |gamma_k| <= C_1 lambda_k for later carriers holds; D(j) != 0 and Lemma 3.3 force |z_j| = 1 and z_j = sgn(gamma_o u_o(j)).  The
formula for o notin K_omega needs Delta d_{m(o)} != 0 (else o is neutral).  The statement does not use the sign of Delta d: for
Delta d_{m(o)} > 0 it forces ANTI-alignment (this is what Proposition 5.8 exploits).

## 4.2 Lemma 4.4 (perturb-and-realign).  CORRECT.
Forced flip at l needs |A_l(p) - A_l(0)| >= (B_l + delta_l H_l)/2 >= n_l delta°_l/2 while only zhat_F moves before the first flip, so
delta°_l <= 2C|p|/n_l; (SF*) second half gives lambda_l <= (5/16) delta°_l 2^{-l-10} <= delta°_l 2^{-l-9}; weights after l(p) are o(|p|); cost by Z3
Lemma 3.1 plus continuity of a.  Carriers between K and l(p) keep eps and stay robust.  (Not used by Theorem 5.6 / Corollary 5.7, which
use banks; it is a standalone tool, and the numerics of degenerate_check4.py illustrate it; re-run: identical output.  Note that its base
point has nu_D/theta = 0.9999987, i.e. a strict non-peak at relative distance 1.3e-6 from degeneracy, the double-precision limit.)

## 4.3 Lemmas 5.4, 5.5 and Theorem 5.6.  CORRECT; the scope must be stated.
Lemma 5.4 re-derived.  No free coordinate: for j notin F, either j in E ⊂ E' ((H2)), or o(j) notin K_omega ∪ Neg (non-neutral by (H1), not
negligible; Prop. 4.2'), or o(j) in K_omega ∪ Neg with j in E' ((H2)) or with factor-32 dominance; in all cases D(j) != 0, so j is a contact.
(T2) at f^(L): (a) fine-owned j: owner re-run, gamma^(L)_o = -lambda_o Delta d^(L) eps_o M^(L) has sign eps_o = z^(L)_j sgn u_o(j), and
|Delta d^(L)| M^(L) >= tau_o C^(L)_1 because tau_o <= tau_{L_0} <= min|Delta d|M/(4 C_1); (b) coarse j with non-neutral non-negligible owner: the
perturbation of gamma_o is <= lambda_o(|Delta d| tau_L/4 + |Delta d^(L) - Delta d|), and |Delta d^(L) - Delta d| <= C_f sum_{l>L} lambda_l <= C_f 2^{-10} tau_L lambda_L <<
tau_L C_1 <= tau_o C_1 for ALL o <= L: this uniformity in o is exactly what (SF_tau) provides (checked); (c) the finitely many coordinates of
E' and of S_o (o in K_omega ∪ Neg, j <= j_0(o)) by convergence; far j in S_o by allowedness (b), uniformly in L.  Costs: dominated convergence;
Fl lies in fine-owned coordinates.  Lemma 5.5 re-derived (first-order raise of the bank carrier only, diagonal base; coarse nu_k move O(mu^2);
later carriers through s_m bounded by (SF*) since min S_{l_b} = s_m; flips o(mu)); precision: rebalance with a 1_F (part 3, 3.3).
Theorem 5.6 = Lemma 5.4 + Lemma 5.5 + Theorem 3.7 (diagonal choice mu_i after L_i): correct.
SCOPE (not stated in V4's theorem or summary; it is in the proof of Lemma 5.4): (H1) + (H2) force D(j) != 0 at EVERY j notin F, hence
|z_j| = 1 off F: Theorem 5.6 is a theorem about MAXIMAL-CONTACT first rows (K = N \ F), typically sign-mixed.  This is precisely the regime
in which V2-ref says the coherent shift residual (C*) is not excluded (at constant-sign maximal contact (C*) does not occur), so Theorem 5.6
is a genuine complement to Master Theorem III' there — for mates with EXACT all-negative data.
NON-GENERICITY (new, proved in V4_ref_notes, Proposition R5): in every maximal-contact z-fibre (|F| >= 2) the set of a for which SOME g in
C(f_a) carries exact two-piece data with Delta d_m < 0 for all m is meagre (Baire argument of Prop. 5.1 with windows on the misaligned side of
zero, plus Prop. 4.2').  Together with the scope remark: the exact-data companion route of Theorem 5.6 can only ever act on a meagre set of
rows; generic rows must be handled by window (approximate) data, i.e. by the V1/V2 framework, whose residual is (C*).

## 4.4 Corollary 5.7.  CORRECT for N = 1; for N >= 2 two precisions.
For N >= 2: (i) "Delta d < 0" must hold in EVERY block (a block with Delta d_m = 0 makes all its non-omega carriers neutral, violating (H1));
so omega must have mass in every block; (ii) non-negligibility of an exceptional strict non-peak not carrying omega reads
|Delta d_{m(k)}||w(k)| >= 2 tau_k C_1 (not |w(k)| >= 2 tau_k).  E = {} (exceptional targets in F) and the factor >= 64 > 32 of Step 6 make E' = {}.
EXISTENCE: rows of Theorem 2.2 type with an EXACTLY degenerate swallowing-type peak are not shown to exist in pure or hysteretic
self-aligned form (Remark 2.3(1) OPEN part).  The same obstruction affects rows that are owner-rule (hysteretic) only above a level K with
coarse z frozen: the threshold still has a jump part from fine flips, which may skip the degenerate value; freezing the fine signs instead
lets fine values cross zero, which (Prop. 4.2') destroys the data.  Prop. 5.1(c) gives exact degeneracy only at FIXED z on all levels, where
the fine carriers are not robust.  So the clause "including exactly degenerate swallowing-type peaks, if present" is a CONDITIONAL statement
(correct as such); whether such rows exist is OPEN (and immaterial: V1's Corollary AC already removes the aligned corner for D_Omega).

## 4.5 Proposition 5.8 (positive mismatch forces dead zones under (FD)).  CORRECT.
Re-derived: |zhat_i| <= 1 + s_i on F (s_i a_i <= nu), so |R| <= (1 + max s)(||y_l||_1 - |y_l(j_l)| + delta_l H_l) < |y_l(j_l)| by (FD), and Prop.
4.2' with Delta d > 0 gives z_{j_l} = -sgn(val_l) sgn(y_l(j_l)), contradiction.  REMARK: (FD) is used ONLY for this negative statement; it is not
needed by any positive result.  A unified design need not contain (FD); without it, carriers whose own new coordinates do not dominate
(|A_l| > B_l + delta_l H_l) can be ANTI-aligned self-consistently, so the obstruction "mixed data always have dead zones" is a feature of
(FD) designs (which, however, density alone makes hard to avoid at coordinates of Z_0 owned by targets close to e_j^*/q*(e_j^*)).

## 4.6 Lemma 4.5 and Proposition 4.6 (sequential projection).  CORRECT; superseded for (B).
Lemma 4.5: at strict non-peaks q_l = eps_l val_l/|R^** zhat|_m = (q_0/sigma_m) eps_l val_l (re-derived from lem:threshold); the cone depends on the
pattern only.  Prop. 4.6: Y4 Lemma 1.8 re-derived (conic decomposition into extreme rays, l_1-norm additive in the orthant, remove mass from the
positive-D rays); the iteration and the description of extreme rays of C ∩ ker D_i (old rays in the kernel and the "sliced" rays of 2-faces)
are standard and correct.  The OPEN "remaining step for (B)" is SUPERSEDED by V2's Theorem B (refereed correct: Hoffman constants through
non-zero minors + Lojasiewicz exactification of all tiny minors at a cheap companion).

## 4.7 Structure of a counterexample (Section 12).  CORRECT as a logical consequence; incomplete as a map of the open core.
It is the contrapositive of cor:D1 + Theorem 5.6 (+ Prop. 5.8 for the dead-zone reading of mixed data).  Two additions are needed for an
accurate picture: (1) by Proposition R5 the first alternative ("no two-piece data with kappa_w <= 1 at f") is the GENERIC one, and for it the
relevant residual is V2-ref's (C*) (window method), not dead zones; (2) "mixed" should read "some Delta d_m < 0 and some Delta d_m >= 0"
(as written), and every all-negative data set at a row with a free coordinate outside the finite set E automatically has a dead zone (the
owner of that coordinate is neutral or negligible).  The "precise remaining step" (stability of nearly exact data at (BT) companions) is a
sensible formulation of the dead-zone gap; V4's suggested route (pulling violated coordinates) leads to infinite support when V is infinite,
as V4 says.
