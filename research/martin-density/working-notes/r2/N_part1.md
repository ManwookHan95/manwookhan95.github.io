# N, part 1: the limit-mate set Ls(f) and the exact reformulation of density

Setting: canonical base, Martin norm p (finite block set I, i.e. p_N, unless said otherwise; everything in this part
holds verbatim for I = N given (T4) = strict convexity of p**). X = c_0, X* = l_1, s(t) := sqrt(1+t^2).
C(f) := {g in X* : p*(f + t g) <= s(t) for all real t} for f in S_{p*}. An operator X -> l_2^2 is written S = (f, g),
S y = (f(y), g(y)); ||S|| = sup_{p(y) <= 1} (f(y)^2 + g(y)^2)^{1/2}; S* e = e^(1) f + e^(2) g for e = (e^(1), e^(2)).
e_theta := (cos theta, sin theta), e_theta^perp := (-sin theta, cos theta). NA := NA((X,p), l_2^2).

Imported (all PROVED in r1, re-checked): (I1) p* is rotund (A_notes Lemma 8.6); (I2) global compactness
(Preprint A Thm 2.1 = A_notes Thm 3.1): f_n -> f in S_{p*}, g_n in C(f_n) => (g_n) has a norm-convergent subsequence and
all limits lie in C(f). Nothing else is used in this part.

## 1.1 Definitions

G := {(f', g') : f' in NA(p) cap S_{p*}, g' in C(f')}  (the "normal-form NA operators").
Ls(f) := {g : there are (f_n, g_n) in G with f_n -> f and g_n -> g in norm}  (f in S_{p*}).
Equivalently Ls(f) = intersection over delta > 0 of cl( union{C(f') : f' in NA cap S_{p*}, p*(f' - f) < delta} ),
and graph(Ls) = cl(G) cap (S_{p*} x X*).

## 1.2 Lemma (normal-form NA operators). PROVED.
(a) Every (f', g') in G is a norm-one operator attaining its norm (at the normer x' of f').
(b) If S in NA, ||S|| = 1, attains at x in S_p and Sx = e_theta (unit vector), then S* e_theta =: h is in NA cap S_{p*}
    (attaining at x), k := S* e_theta^perp is in C(h), and Q_theta S = (h, k) where Q_theta is the rotation with
    Q_theta e_theta = e_1, Q_theta e_theta^perp = e_2. So every norm-one NA operator is a rotation of an element of G.
*Proof.* (a) ||(f',g')|| <= 1 by definition of C(f') (sup over theta of p*(cos theta f' + sin theta g') <= 1 is the same as
p*(f' + t g') <= s(t) for all t, the case cos theta = 0 being the limit t -> infinity), and >= p*(f') = 1. If f'(x') = 1 = p(x'),
then g'(x')^2 <= p(x')^2 - f'(x')^2 = 0 (the primal form of the mate inequality: f'(y)^2 + g'(y)^2 <= p(y)^2, which is
||(f',g')|| <= 1 tested at y), so |(f',g')x'| = 1.
(b) h(x) = <Sx, e_theta> = 1 and p*(h) <= ||S|| = 1; so h attains its norm 1 at x. (Q_theta S) y = (<Sy, e_theta>, <Sy, e_theta^perp>)
= (h(y), k(y)), and ||Q_theta S|| = ||S|| = 1, so k in C(h). QED.

## 1.3 Theorem 1 (exact reformulation). PROVED.
Let f in S_{p*} and g in C(f).
(i) If g in Ls(f), then (f, g) is in cl NA.
(ii) If 0 <= rho < 1 and (f, rho g) is in cl NA, then rho g in Ls(f).
(iii) g in Ls(f)  <=>  (f, rho g) in cl NA for every rho in (0,1).
(iv) More generally, if (f, g) in cl NA and the only unit vectors e with p*((f,g)* e) = 1 are +-e_1, then g in Ls(f).
(v) NA((X,p), l_2^2) is dense in L((X,p), l_2^2)  <=>  Ls(f) = C(f) for every f in S_{p*}.
(vi) (Global compactness) Ls(f) is a compact, symmetric subset of C(f), star-shaped about 0 (lambda Ls(f) in Ls(f) for
     lambda in [0,1]); in the definition of Ls(f) "g_n -> g in norm" may be replaced by "g_n -> g weak*".

*Proof.* (i) Let (f_n, g_n) in G, f_n -> f, g_n -> g. By Lemma 1.2(a), (f_n, g_n) in NA, and
||(f_n, g_n) - (f, g)|| <= (p*(f_n - f)^2 + p*(g_n - g)^2)^{1/2} -> 0.

(ii) Put S := (f, rho g). First, the norming set of S* is {+-e_1}: for theta not in pi Z with cos theta != 0, writing
tau := tan theta, p*(S* e_theta) = |cos theta| p*(f + tau rho g) <= |cos theta| s(rho tau) < |cos theta| s(tau) = 1 (as g in C(f),
so rho g in C(f) is applied at the parameter rho tau; and s(rho tau) < s(tau) because rho < 1, tau != 0); for cos theta = 0,
p*(S* e_theta) = rho p*(g) <= rho < 1 (p*(g) <= 1 for every mate: let t -> infinity in p*(f/t + g) <= s(t)/t). And
p*(S* e_1) = p*(f) = 1, so ||S|| = 1.
Let S_n in NA with S_n -> S; for n large ||S_n|| > 0. Let S_n attain its norm at x_n in S_p and put e_n := S_n x_n/|S_n x_n|.
Replacing x_n by -x_n we may assume <e_n, e_1> >= 0. Then p*(S* e_n) >= p*(S_n* e_n) - ||S_n - S|| = ||S_n|| - ||S_n - S|| -> 1
(note p*(S_n* e_n) >= <S_n* e_n, x_n> = |S_n x_n| = ||S_n||). Every cluster point e of (e_n) is a unit vector with
p*(S* e) >= 1, hence e = e_1 by the first step and <e, e_1> >= 0. So e_n -> e_1. Let theta_n with e_n = e_{theta_n},
theta_n -> 0. By Lemma 1.2(b) applied to S_n/||S_n||: h_n := S_n* e_n/||S_n|| in NA cap S_{p*} and
k_n := S_n* e_n^perp/||S_n|| in C(h_n). Since S_n -> S in operator norm, ||S_n|| -> 1 and e_n -> e_1:
h_n -> S* e_1 = f and k_n -> S* e_2 = rho g in norm. Thus rho g in Ls(f).

(vi) Symmetry and star-shape: C(f') is convex, symmetric and contains 0, so (f_n, lambda g_n) in G when (f_n, g_n) in G and
|lambda| <= 1. Ls(f) in C(f): if f_n -> f, g_n -> g in norm, then p*(f + t g) = lim p*(f_n + t g_n) <= s(t). Closedness:
graph(Ls) is the closure of G intersected with S_{p*} x X*, so each Ls(f) is closed (diagonal argument: if g^j in Ls(f),
g^j -> g, pick (f^j, h^j) in G with p*(f^j - f) + p*(h^j - g^j) < 1/j). Closed subset of the compact C(f) (by I2), hence
compact. Weak* version: if (f_n, g_n) in G, f_n -> f and g_n -> g weak*, then by (I2) a subsequence of (g_n) converges in
norm, necessarily to g; so g in Ls(f).

(iii) (=>) rho g in Ls(f) by (vi) (star shape), so (f, rho g) in cl NA by (i) applied to rho g in C(f).
(<=) By (ii), rho g in Ls(f) for all rho < 1; Ls(f) is closed, so g in Ls(f).

(iv) The proof of (ii) used rho < 1 only to show that the norming set of S* is {+-e_1}.

(v) (=>) Let f in S_{p*}, g in C(f). For rho < 1, (f, rho g) is an operator, hence in cl NA by density; by (ii) rho g in Ls(f);
by closedness g in Ls(f). So C(f) in Ls(f), and Ls(f) in C(f) by (vi).
(<=) Let S be a nonzero operator. S* attains its norm on the compact unit circle at some e_theta; then
Q_theta S/||S|| = (f, g) with f = S* e_theta/||S|| in S_{p*} and g in C(f) (Lemma 1.2(b) without attainment: the computation
of Q_theta S only uses ||S|| = p*(S* e_theta)). By hypothesis g in Ls(f), so (f, g) in cl NA by (i). NA is invariant under
rotations of l_2^2 and under positive scaling, and these maps are isometries / homeomorphisms of the operator space, so
S in cl NA. QED.

Remark 1.4 (the case rho = 1). Whether (f, g) in cl NA implies g in Ls(f) when S* = (f,g)* has norming directions other than
+-e_1 (e.g. when theta -> p*(cos theta f + sin theta g) is identically 1) is not decided here; by (iii)-(v) it is irrelevant for
the density question. Note that if (f,g) in cl NA and e_theta is a cluster point of the norming directions e_n of
approximating NA operators, the proof of (ii) gives k in Ls(h) with h = cos theta f + sin theta g, k = -sin theta f + cos theta g.

## 1.5 Proposition 2 (Ls(f) is a union of lower limits). PROVED.
Let A(f) be the set of Hausdorff limits A = lim_n C(f_n) taken along sequences f_n in NA cap S_{p*}, f_n -> f, along which the
compact convex sets C(f_n) converge in the Hausdorff metric (of p* on X*). Then:
(a) A(f) is nonempty and compact (in the Hausdorff metric); each A in A(f) is a compact, convex, symmetric subset of C(f);
(b) Ls(f) = union of all A in A(f);
(c) (finite non-recovery certificate) g in C(f) is NOT in Ls(f) iff there are finitely many x_1, ..., x_k in X = c_0 and
    delta > 0 such that every f' in NA cap S_{p*} with p*(f' - f) < delta satisfies max_i ( g(x_i) - r~_{f'}(x_i) ) >= delta,
    where r~_{f'}(x) = max{h(x) : h in C(f')} = inf{ sum_j (p(y_j)^2 - f'(y_j)^2)^{1/2} : sum_j y_j = x } (A_notes Prop 2.2).
(d) cl conv Ls(f) = C(f)  <=>  for every x in X: sup_{A in A(f)} h_A(x) = r~_f(x) (h_A the support function), and in that case
    every extreme point of C(f) lies in Ls(f).
*Proof.* Q := union over n of C(f_n) union C(f) is norm compact for every convergent sequence f_n -> f (I2), so the hyperspace
of its nonempty compact subsets is compact (Blaschke); NA cap S_{p*} is dense in S_{p*} (Bishop-Phelps), so A(f) is nonempty.
(a) Limits of convex symmetric sets are convex symmetric; they lie in C(f) by (I2). Compactness of A(f): let A^j in A(f),
A^j = lim_n C(f^j_n). Choose n_j with p*(f^j_{n_j} - f) < 1/j and d_H(C(f^j_{n_j}), A^j) < 1/j. Then f^j_{n_j} -> f, so by (I2)
the sets C(f^j_{n_j}) lie in one compact set Q; by Blaschke a subsequence C(f^j_{n_j}) -> A' (Hausdorff), so A' in A(f), and
A^j -> A' along that subsequence. (The same diagonal argument shows that A(f) is closed.)
(b) If g in A = lim C(f_n), then dist(g, C(f_n)) -> 0, so g in Ls(f). Conversely if (f_n, g_n) in G, f_n -> f, g_n -> g, pass
(Blaschke, inside the compact Q) to a subsequence with C(f_n) -> A; then g in A.
(c) (<=) If g in Ls(f), g = lim g_n with g_n in C(f_n), f_n NA -> f; for large n, p*(f_n - f) < delta, while
g(x_i) - r~_{f_n}(x_i) <= g(x_i) - g_n(x_i) <= p*(g - g_n) p(x_i) -> 0 for each i; contradiction.
(=>) For A in A(f), g not in A (by (b)); A is weak*-compact convex, so Hahn-Banach separation in (l_1, weak*) gives x_A in c_0
with g(x_A) > h_A(x_A). The set O_A := {B : g(x_A) - h_B(x_A) > eta_A}, eta_A := (g(x_A) - h_A(x_A))/2, is Hausdorff-open
(|h_B(x) - h_{B'}(x)| <= d_H(B, B') p(x)) and contains A. By compactness of A(f) finitely many O_{A_1},...,O_{A_k} cover A(f).
If no delta > 0 worked, there would be NA f'_n -> f with C(f'_n) outside the open set O := union O_{A_i}; a Blaschke-convergent
subsequence has a limit in A(f), which lies in O, so C(f'_n) is in O eventually: contradiction. Take x_i := x_{A_i},
delta := min(eta_{A_i}, delta_0) with delta_0 from this argument (h_{C(f')} = r~_{f'}).
(d) h_{cl conv Ls(f)} = sup_A h_A by (b); two compact convex sets coincide iff their support functions on c_0 coincide.
If cl conv Ls(f) = C(f), Milman's converse of the Krein-Milman theorem gives ext C(f) in cl Ls(f) = Ls(f). QED.

Remark 1.6. Ls(f) need not be convex a priori (it is a union of convex sets). Density at f requires every g in C(f) to be
in SOME A in A(f) (one sequence per mate), which is weaker than the condition of A_notes Cor 3.3 (one sequence for all
mates). Condition (d) ("single-direction recovery": for each x in c_0 separately an NA sequence with
liminf r~_{f_n}(x) >= r~_f(x)) is exactly the k = 1 case of A_notes Cor 3.3(b); it yields the extreme mates only.

## 1.7 Corollary 3 (lower bounds for Ls(f) imported from r1). PROVED (given the cited r1 theorems).
For every f in S_{p*}: cl Cert^sh(f) is contained in every A in A(f), hence in Ls(f) (Transport Theorem 4.10 and Theorem 4.17 of
A_notes: cl Cert^sh(f) is in Li_n C(f_n) for EVERY sequence f_n -> f). This includes finite, shifted and weighted certificates,
locally admissible linear decompositions (A Thm 6.5) and the averaging class of A Thm 6.8 (with the coordinatewise radius, referee
fix G1), and the locally split mates of D Thm 11.6 (D's proof recovers them along canonical truncations; they are also in
cl Cert(f) by A's Theorem L when the split is linear). Ls(f) = C(f) holds for f in NA (KLMW: C(f) in Li of the constant
sequence) and for f in Preprint A's residual set Omega (Hausdorff continuity of C there).
In particular: Def(f) := C(f) \ Ls(f) is contained in C(f) \ cl Cert^sh(f), the set studied in A_notes §7.
