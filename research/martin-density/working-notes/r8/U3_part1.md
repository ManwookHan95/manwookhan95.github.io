# U3 part 1 — Exact rigidity of two-piece data, profile constancy, and failure of lower semicontinuity along block-tame rows

Setting: paper/martin_density_note.tex (notation as there), finite block set I = {1..N}, p = p_N; T admissible (for 1.1-1.4 any
admissible T; for 1.5 an SLD-type design with (SF*), (Z0) as in V4, e.g. D_Omega / D^{V2} augmented by V4's conditions); base
operator U arbitrary in 1.1-1.4, diagonal in 1.5.  Conventions: two-piece data (b^+-, omega^+-) as in Definition def:twopiece; the
DATA convention Delta_m := d_m(omega^-_m) - d_m(omega^+_m); psi_m := R_m^* w_m in l_1 (the block shift vector of f); for a pair of
data put Sigma(omega) := F ∪ ⋃_m ⋃_{k in supp omega^+_m ∪ supp omega^-_m} supp u_{k,m}.

## 1.1 Lemma S (exact rigidity / sandwich).  PROVED (any admissible T).
Let f in S_{p*} have F finite and let h in X* carry two-piece data (b^+-, omega^+-).  Put c^+-(j) := sum_m d_m(omega^+-_m) psi_m(j)
and W_Delta := sum_m Delta_m psi_m.  Then for every j notin Sigma(omega):
 (a) h(j) = b^+(j) - c^+(j) = b^-(j) - c^-(j);
 (b) if j is a free coordinate (|z_j| < 1): b^+(j) = b^-(j) = 0, hence h(j) = -c^+(j) = -c^-(j) and W_Delta(j) = 0;
 (c) if j is a contact (|z_j| = 1): z_j (h(j) + c^+(j)) >= 0 >= z_j (h(j) + c^-(j)); in particular z_j W_Delta(j) <= 0.
Proof.  At j notin Sigma(omega), (R_m^* omega^+-_m)(j) = sum_k lambda_{k,m} omega^+-_m(k) u_{k,m}(j) = 0 for every m, so the two
representations h = b^+- + sum_m R_m^*(omega^+-_m - d_m(omega^+-_m) w_m) read h(j) = b^+-(j) - c^+-(j): (a).  Side admissibility
(Definition def:twopiece): b^+-(j) = 0 for j notin F ∪ K, which gives (b); z_j b^+(j) >= 0 >= z_j b^-(j) for j in K, which gives the
first part of (c).  Subtracting, z_j (c^+(j) - c^-(j)) >= 0, and c^+ - c^- = -W_Delta.  QED
(This is V2's Proposition C3 together with the sandwich inequalities themselves; the point here is that it needs NO smallness or
dominance hypothesis and holds at every coordinate outside Sigma(omega).)

## 1.2 Corollary S1 (one block: the profile is constant unless the data are shifted).  PROVED (N = 1, any admissible T).
Let N = 1, f with F finite, h with two-piece data, psi := R^* w, Delta := d(omega^-) - d(omega^+).  For j notin Sigma(omega) with
psi(j) != 0 put pi_h(j) := h(j)/psi(j) (the PROFILE of h at j).  Call a contact j ALIGNED if z_j psi(j) > 0 and ANTI-ALIGNED if
z_j psi(j) < 0.  Then, for j notin Sigma(omega) with psi(j) != 0:
 (i)   j free: Delta = 0 and pi_h(j) = -d(omega^+) = -d(omega^-);
 (ii)  j aligned contact: -d(omega^+) <= pi_h(j) <= -d(omega^-) (so Delta <= 0);
 (iii) j anti-aligned contact: -d(omega^-) <= pi_h(j) <= -d(omega^+) (so Delta >= 0).
Consequently: the oscillation of pi_h over the aligned contacts outside Sigma(omega) is at most |Delta|; and if, outside
Sigma(omega), there is a free coordinate or an anti-aligned contact with psi != 0, then Delta <= 0 forces Delta = 0 as soon as one
aligned contact exists, and pi_h is CONSTANT (= -d(omega^+)) on all free coordinates and all (aligned or anti-aligned) contacts outside
Sigma(omega) with psi != 0.
Proof.  Lemma S with c^+-(j) = d(omega^+-) psi(j).  (i) is (b).  (ii): divide z_j(h(j) + d^+ psi(j)) >= 0 and z_j(h(j) + d^- psi(j)) <= 0
by z_j psi(j) > 0.  (iii): the same with z_j psi(j) < 0, which reverses both inequalities.  The interval in (ii) is non-empty only if
d^- <= d^+, the one in (iii) only if d^+ <= d^-.  QED

## 1.3 Corollary S2 (finitely many contacts: no switching, no shift).  PROVED (any admissible T, any N).
If F and K are finite (in particular at every norm-attaining f, Proposition prop:smooth(c)), every pair of two-piece data has
b^+ = b^-, omega^+ = omega^- and Delta_m = 0 for every m.
Proof.  v := b^+ - b^- = sum_m R_m^*(omega^-_m - omega^+_m) - W_Delta lies in Y (each R_m^* maps into Y) and is supported in the finite
set F ∪ K (side admissibility).  By (T-c), v = 0.  Then L^* applied to (Delta_m w_m - (omega^-_m - omega^+_m))_m vanishes; L^* is
injective on V^* (eq:Lstar), so Delta_m w_m = omega^-_m - omega^+_m for each m.  The right side is finitely supported in Q_m, while
w_m = +-M_m != 0 on the non-empty peak set P_m; hence Delta_m = 0 and omega^-_m = omega^+_m.  QED
(At NA rows exact data cannot carry ANY shift or switching; scale-dependent structure of mates of NA rows lives only in their
decompositions at positive scales.  This is the precise sense of Remark rem:onesided(a).)

## 1.4 Proposition S3 (necessary condition for following a non-constant profile).  PROVED (N = 1, any admissible T).
Let f in S_{p*} have F finite, g in C(f), rho in (0,1], and let s_1, s_2 be coordinates with psi(s_1), psi(s_2) != 0 and
pi_g(s_1) != pi_g(s_2) (pi with respect to psi = R^* w of f).  Let f_n -> f be rows with F_n finite at which every mate carries
two-piece data (e.g. (BT) rows, Theorem thm:onesided(c)), and let Q_n be the strict non-peak set of f_n and
Sigma_n := F_n ∪ ⋃_{k in Q_n} supp u_k.  Suppose that for infinitely many n:
 (1) s_1, s_2 notin Sigma_n, and each of them is a free coordinate or a contact of f_n; and
 (2) outside Sigma_n, f_n has an aligned contact and, in addition, a free coordinate or an anti-aligned contact with psi_n != 0
     (alignment taken with respect to psi_n := R^* w^{(n)} and z^{(n)}).
Then rho g notin Li_n C(f_n); quantitatively, along those n,
     dist_{l_1}(rho g, C(f_n)) >= (rho kappa_0 - rho ||g||_inf (|psi_n - psi|(s_1) + |psi_n - psi|(s_2)))/2,
     kappa_0 := |psi(s_1) psi(s_2)| |pi_g(s_1) - pi_g(s_2)| > 0,
and the right side tends to rho kappa_0/2 (psi_n -> psi in l_1, Proposition prop:continuity).
Proof.  Let G in C(f_n) and take two-piece data of G at f_n.  Their omega-supports lie in Q_n, so Sigma(omega) ⊂ Sigma_n.  By (2) and
Corollary S1 (applied at f_n), Delta = 0 and pi^{(n)}_G is constant on the free coordinates and contacts outside Sigma_n with psi_n != 0;
by (1) this applies at s_1, s_2 if psi_n(s_i) != 0, and then G(s_1) psi_n(s_2) - G(s_2) psi_n(s_1) = 0.  If psi_n(s_i) = 0 for some i,
Lemma S(a)-(c) with Delta = 0 gives G(s_i) = -d^+ psi_n(s_i) = 0, and the same identity holds.  The functional
Lambda_n(h) := h(s_1) psi_n(s_2) - h(s_2) psi_n(s_1) satisfies |Lambda_n(h)| <= ||h||_1 (|psi_n(s_1)| + |psi_n(s_2)|) <= 2 ||h||_1 since
||psi_n||_inf <= sum_k lambda_k ||u_k||_inf <= 1.  Hence 2 ||G - rho g||_1 >= |Lambda_n(rho g)|, and |Lambda_n(rho g)| >= rho kappa_0 -
rho ||g||_inf (|psi_n - psi|(s_1) + |psi_n - psi|(s_2)).  QED
Reading.  To recover a mate whose profile is not constant on {s_1, s_2}, approximants at which mates have exact data must, for all
large n, either put s_1 or s_2 into Sigma_n (make it a support coordinate — a bank — or cover it by the support of a strict
non-peak), or be ALIGNED WITH MAXIMAL CONTACT outside Sigma_n (no free coordinate and no anti-aligned contact with psi_n != 0).
The engineered approximants of Section sec:engineered use the first alternative (window masses = banks on contacts); NA rows can
only use the first alternative (they have cofinitely many free coordinates, Corollary S2).

## 1.5 Theorem NL (failure of lower semicontinuity at a self-aligned row along block-tame rows).  PROVED
(design with (SF*), (Z0); diagonal U; N = 1; uses only V4's refereed Construction SA / Theorem 2.2 / Proposition 3.2 and the
hysteretic re-run of Proposition 5.3.)
Let f := f_SA (V4 Construction SA(1, eta), Theorem 2.2; N = 1), with its exceptional carrier l_- (target y*, strict non-peak, q < 0)
and k_- := k(l_-).  Then there are rows f_n -> f satisfying (BT) (hence f_n in Rec by Corollary cor:BTrecovered) such that for every
g in C(f) whose profile is non-constant on two coordinates s_1, s_2 of a signature set S_l (l != l_-), and every rho in (0,1],
     liminf_n dist(rho g, C(f_n)) >= rho kappa_0(g; s_1, s_2)/2 > 0.
Such g exist: the coherent-shift mates of V4 Proposition 3.2 with a coordinate-dependent split chi.  In particular the fibre map
f' -> C(f') is NOT lower semicontinuous at the block-tame row f along this sequence of block-tame rows, although every mate of f is
recovered along the engineered approximants of f.
Proof.  Step 1 (the rows f_n).  Recall from Construction SA: F = {p, p'} ⊂ Z_0, every carrier except l_- is owner-assigned with sign
eps_l, z = eps_l on S_l, and n_{l_-} val_{l_-} = y*(zhat_F) + delta_{l_-} H_{l_-} = -eta, so y*(zhat_F) = -(eta + delta_{l_-} H_{l_-}) < 0.
Since y* occurs as a target at infinitely many carriers of the block (Theorem 2.2 Step 1: infinitely many carriers have target y*),
choose such carriers o_n -> infinity, o_n > l_-, with delta_{o_n} H_{o_n} < (eta + delta_{l_-} H_{l_-})/2.  For these, supp y* = F, so
B_{o_n} = 0, A_{o_n} = y*(zhat_F) < 0, eps_{o_n} = -1 and z = -1 on S_{o_n} in f.
Define f_n: same a; z^{(n)} := z except: z^{(n)} := +1 on S_{o_n}, and the coordinates owned by carriers l > o_n are re-assigned by the
HYSTERETIC re-run of V4 Proposition 5.3 (reference signs eps_l of f; keep eps_l unless eps_l A_l <= -(B_l + delta_l H_l)/2, in which
case eps_l := sgn A_l).  Coordinates owned by carriers < o_n are unchanged (allowedness (a): coarser targets avoid S_{o_n}; disjoint
signatures), so z^{(n)} -> z coordinatewise and a^{(n)} = a; by Remark rem:lemmaZ(c), f_n -> f in S_{p*}.
Step 2 (f_n is (BT)).  Values of carriers < o_n are unchanged.  n val_{o_n}^{(n)} = A_{o_n} + delta_{o_n} H_{o_n} <= -(eta + delta_{l_-}
H_{l_-})/2 < 0 while z^{(n)} = +1 on S_{o_n}: o_n is an exactly swallowed ANTI-TYPE carrier with |val| >= eta/(2 n_{o_n}), hence a peak
(nu = m|val|/Phi_{o_n} -> infinity relative to theta; Theorem 2.2 Step 3 bounds theta) with margin >= q_0 eta/4.  Every re-run carrier
l > o_n has n_l |val_l| >= (B_l + delta_l H_l)/2 with sign eps_l (Proposition 5.3's re-run, which uses only the owner recursion,
allowedness and (SF*)), hence is a swallowing-type peak with margin >= q_0 delta°_l/4 (Theorem 2.2 Step 4 with |val_l| >= delta°_l/2).
The threshold theta^{(n)} -> theta (zeta^{(n)} -> zeta in l_1), so the finitely many carriers whose status is not robust by Step 4
(the first carrier of the block and l_-) keep their statuses for large n.  Thus Q^{(n)} = {k_-}, there is no degenerate peak, and
(MS) holds (Theorem 2.2 Step 8 with margins >= q_0 delta°_l/4 beyond a finite set): f_n satisfies (BT).
Step 3 (alignment at f_n).  Sigma_n = F ∪ supp u_{l_-} = F ∪ S_{l_-} (Q^{(n)} = {k_-}, supp y* = F).  Every coordinate off F is a
contact of f_n (the owner recursion assigns +-1 everywhere, V4 Lemma 1.2).  For s in S_c (c a carrier other than l_-, owner c):
psi_n(s) = lambda_c w^{(n)}(c) v_c(s) + sum_{l > c} lambda_l w^{(n)}(l) y_l(s)/n_l, and by the dominance estimate of Theorem 2.2 Step 6
(which bounds MODULI of the later terms using allowedness (b) and (SF*); |w| <= 1) the later sum is at most 2^{-5} lambda_c v_c(s) <=
2^{-4} lambda_c |w^{(n)}(c)| v_c(s) (|w(c)| = M >= 1/2 at peaks).  Hence sgn psi_n(s) = sgn w^{(n)}(c) = sgn val^{(n)}_c, psi_n(s) != 0.
For every swallowing-type peak c (all carriers except l_- and o_n) the contacts of S_c are ALIGNED; the contacts of S_{o_n} are
ANTI-ALIGNED (z = +1, w(o_n) = -M).  Both lie outside Sigma_n.  So hypothesis (2) of Proposition S3 holds at every f_n, and (1) holds
for any s_1, s_2 in S_l, l != l_-, once o_n > l (they are aligned contacts of f_n and of f).
Step 4 (conclusion).  Proposition S3.  Existence of g: in V4 Proposition 3.2 the split chi: F^c -> [0,1] may be chosen coordinatewise
(b^+ := chi Delta_alpha lambda_{l_-} V 1_{F^c} + beta^+ is z-signed because V 1_{F^c} is z-signed and chi >= 0; b^- = b^+ - Delta_alpha
lambda_{l_-} V = (chi - 1) Delta_alpha lambda_{l_-} V 1_{F^c} + beta^- is (-z)-signed because chi <= 1); part (iv) of that proposition gives
c g in C(f) for small c > 0.  At s in S_l (l != l_-), u_{l_-}(s) = 0 and omega^+ vanishes, and V = u_{l_-} - (val_{l_-}/|zeta^|) psi, so
     g(s) = chi_s Delta_alpha lambda_{l_-} V(s) - d(omega^+) psi(s) = psi(s) ( -d(omega^+) + chi_s Delta_alpha lambda_{l_-} |val_{l_-}|/|zeta^| )
EXACTLY.  Hence pi_g(s_1) - pi_g(s_2) = (chi_{s_1} - chi_{s_2}) Delta_alpha lambda_{l_-} |val_{l_-}|/|zeta^| != 0 when chi_{s_1} != chi_{s_2}.  QED
Remarks.  (a) The same proof gives non-recovery along ANY sequence of rows with exact data for all mates which contain, at least
once per row, an exactly swallowed anti-type robust peak (or a free coordinate with psi_n != 0) outside Sigma_n, while keeping two
aligned contacts s_1, s_2 outside Sigma_n.  So the Baire-generic rows of V4 Proposition 5.1 (fixed z, perturbed a; they acquire
anti-type peaks, Part 2) and NA rows without banks on {s_1, s_2} cannot be used to recover oscillating mates.
(b) Theorem NL does not contradict f in Rec (f is (BT)): the engineered approximants of f put window masses (banks) on contacts, i.e.
use the first alternative of Proposition S3, and keep all far carriers aligned.  Any recovery proof for (C*) rows must therefore
use approximants that (i) keep every peak of a shifted block exactly swallowed and ALIGNED at the fine levels (no fine anti-type
robust peak of a shifted block and no fine free coordinate with psi != 0 outside the omega-supports) or (ii) bank the oscillation
coordinates.  This is a precise version of "the approximating sequence must be engineered", and it explains why lower
semicontinuity along the dense set of (BT) rows (V4 Proposition 5.3) cannot be expected for an ARBITRARY dense sequence; Proposition
5.3's own re-alignment keeps the reference signs (hysteresis) and is aligned in this sense.
(c) Numerical check: U3_work/nl_check.py (Part 5).
