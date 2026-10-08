
---

## 6. Mate fibres at tame points: finite certificates

**Lemma 6.1 (excess splitting). [PROVED]** Let eta be the normer of f (eta = x' or xi) with data as in 1.3. For
every nu in X** (resp. X):
  Delta(eta + nu) := p**(eta + nu) - f(eta + nu) = E_q(nu) + sum_m E_m(R_m** nu),
with E_q(nu) = q**(eta+nu) - c - a(nu) >= 0 and E_m(delta) = |z_m + delta|_m - sigma_m - w_m(delta) >= 0.
Proof. p**(eta) = 1 = f(eta) = c + sum sigma_m, f = a + sum R_m^* w_m, p** = q** + sum |R_m** .|_m. []
Since f(eta + t nu) = 1 + t f(nu): if f(nu) = 0 then Delta(eta + t nu) = phi(t nu) (resp. phi'(t nu)).

**Definition 6.0.** For a block m at eta: the margin of a peak k is mu_{k,m} := |u_{k,m}(eta)| - theta_m Phi_m(k)
(1.3). eta satisfies **margin sparsity (MS)** in block m if sum_{k in P°_m, mu_{k,m} < s} Phi_m(k) = o(s) as s -> 0+.
eta (or f) is **tame** if: (T1) a in c_00; (T2) the kink set K is finite; (T3) for every m the set
Qbar_m := Q_m cup Dg_m of strict non-peaks and degenerate peaks is finite; (T4) (MS) holds in every block.
For eta = x' in c_0, (T1) and (T2) are automatic.
Let J := N \ (F cup K) (free coordinates) and

  W(eta) := span{e_j^* : j in F cup K} + span{u_{k,m} : k in Qbar_m, m in I} + span{R_m^* w_m : m in I}   (finite-dimensional).

**Theorem 6.2 (Theorem A: tame NA points). [PROVED]** If f' in S_{p*} attains its norm at a tame x' in c_0, then
C(f') is contained in W(x').

Proof. Let psi_1,...,psi_N be the restrictions to the coordinates in J' of the functionals
u_{k,m} (k in Qbar'_m, m in I) and R_m^* w'_m (m in I), and V := {v in c_0 : supp v in J', psi_i(v) = 0 for all i}.
Fix v in V and t != 0 small.
Base: a'(v) = 0 (supp a' = F' is disjoint from J'), and since z' in c_0 the room r' := min_{J'} (1 - |z'_j|) is
positive; for |t| ||v||_inf <= c' r' Lemma 4.1 gives E_q(tv) = 0.
Block m: delta := t R_m v vanishes on Qbar'_m (u_{k,m}(v) = 0 there) and
0 = w'_m(R_m v) = M'_m sum_{P'_m} s_k (R_m v)_k + sum_{Q'_m} w'_m(k)(R_m v)_k = M'_m S_{P'}(R_m v);
so delta is supported in P°'_m with zero peak sum. By (5.1) (Lemma 5.2 with mu = 0),
E_m(t R_m v) <= 2 m |t| q(v) sum_{k in P°'_m : mu'_{k,m} < |t| q(v)} Phi_m(k) = o(t^2) by (MS).
Also f'(v) = a'(v) + sum_m w'_m(R_m v) = 0. Hence by Lemma 6.1, p(x' + tv) - 1 = Delta'(x'+tv) = o(t^2).
For g' in C(f') (g'(x') = 0, Lemma 2.1): t^2 g'(v)^2 = g'(x'+tv)^2 <= p(x'+tv)^2 - 1 = o(t^2), so g'(v) = 0.
Thus g'|_{c_0(J')} vanishes on the finite-codimensional subspace V of c_0(J'); by linear algebra in the dual pair
(c_0(J'), l_1(J')) it is a combination sum_i c_i psi_i. Then g' - sum_i c_i (corresponding functional) vanishes on
c_0(J'), i.e. is supported in the finite set F' cup K', hence lies in span{e_j^* : j in F' cup K'}. []

**Remark 6.3 (absorption by free coordinates). [PROVED content of the proof]** The proof shows *why* mates at
NA points are so constrained: the base is exactly flat on the infinitely many free coordinates of x' (room ~1 far
out), and by the independence lemma (F5) any finite set of block functionals restricted to the free coordinates
is linearly independent; so every direction can be corrected by a free-coordinate vector so as to become
invisible to the non-peaks and to the peak sum. Such directions are second-order flat (only peak overshoots,
o(t^2) under (MS)), hence killed by all mates. Consequence: **every mate at a tame NA point is a finite
certificate** (a finite combination of support coordinates, non-peak block functionals and R_m^* w'_m). To
approximate a mate g of f that is not (close to) such a finite combination, the NA approximants must be
non-tame: infinitely many non-peaks, or many near-threshold peaks (failure of (MS)), engineered by the free far
coordinates of z' (R4).

**Numerical confirmation** (C_work/thmA_test.py; n = 7, d = 3, one block with 5 coordinates, all peaks): the
subspace V' (free coordinates, w'(Rv) = 0) has dimension 3 and the excess along each of its basis vectors is
exactly 0 (|.| < 3e-16) for t up to 0.3, while a generic direction has excess/t^2 between 0.12 and 1.19.

**Theorem 6.4 (Theorem C: tame non-attaining supports). [PROVED]** If f in S_{p*} has a tame normer xi, then
C(f) is contained in W(xi). In particular C(f) is finite-dimensional.

Proof. Same as Theorem 6.2 with two changes. (i) Room: xi need not have uniform room, so work with
V_00 := {nu in c_00(J) : psi_i(nu) = 0}; for nu in V_00 only finitely many coordinates move and Lemma 4.1 applies
for small t (each moved coordinate has |z_j| < 1). The block computation is identical (R_m** nu = R_m nu, margins
mu_{k,m} at xi, (MS) at xi), so phi(t nu) = o(t^2), nu in ker f, and g(nu) = 0 for g in C(f) by Lemma 3.6.
(ii) Density: by (F5) the psi_i are linearly independent on c_00(J), so there are nu^1,...,nu^N in c_00(J) with
psi_i(nu^j) = delta_ij; for nu in V_0 := {nu in c_0(J) : psi_i(nu) = 0}, truncations nu_n -> nu in c_0 and
nu_n - sum_i psi_i(nu_n) nu^i in V_00 converge to nu. So g (continuous on c_0) vanishes on V_0, and the
linear-algebra step of Theorem 6.2 applies. []

**Lemma 6.6 (rebalancing directions). [PROVED]** Let xi be tame and m_0 in I, lambda real. There is
nu = lambda xi + nu_J with nu_J in c_00(J) such that f(nu) = 0, phi(t nu) = o(t^2) as t -> 0, and for every
g = b + sum_m R_m^* v_m in W(xi) (b supported in F cup K, v_m = omega_m + c_m w_m, omega_m supported in Qbar_m):

  g(nu) = lambda g(xi) - (lambda/sigma_{m_0}) v_{m_0}(z_{m_0}).

Proof. Let pi_m := sum_{k in P_m} s_k m Phi_m(k) u_{k,m} (so pi_m(y) = S_{P_m}(R_m y)); it is an absolutely
convergent series in l_1. By (F5), the restrictions to J of {u_{k,m} : k in Qbar_m} cup {pi_m} are linearly
independent (a relation would give an element of Y vanishing on the cofinite set J, hence 0, and the
T-coefficients at the infinitely many (k,m), k in P°_m, force the pi_m-coefficients to vanish, then the others).
So we can choose nu_J in c_00(J) with
  u_{k,m}(nu_J) = -(lambda/sigma_m) u_{k,m}(xi) [m = m_0] (k in Qbar_m),   pi_m(nu_J) = -(lambda/sigma_m) pi_m(xi) [m = m_0],
where [m = m_0] is 1 or 0. Put nu := lambda xi + nu_J.
* f(nu) = lambda + a(nu_J) + sum_m w_m(R_m nu_J), a(nu_J) = 0, and
  w_m(R_m nu_J) = M_m pi_m(nu_J) + sum_{k in Q_m} w_m(k) m Phi_m(k) u_{k,m}(nu_J) equals 0 for m != m_0 and
  -(lambda/sigma) w(z) = -lambda for m = m_0. So f(nu) = 0.
* Base: xi + t nu = (1 + t lambda)(xi + t nu_J/(1+t lambda)), so E_q(t nu) = 0 for small t (Lemma 4.1 and homogeneity).
* Block m != m_0: R_m**(t nu) = t lambda z_m + t R_m nu_J with R_m nu_J vanishing on Qbar_m and of zero peak sum;
  Lemma 5.2 (mu = t lambda) and (MS) give E_m = o(t^2).
* Block m_0: R**(t nu) = t(lambda - lambda/sigma) z + t delta'' with delta'' := R nu_J + (lambda/sigma) z, which vanishes
  on Qbar and has zero peak sum, and |delta''_k| <= m Phi_k (q(nu_J) + |lambda| q**(xi)/sigma); Lemma 5.2 and (MS)
  give E_{m_0} = o(t^2).
* By Lemma 6.1, phi(t nu) = o(t^2).
* g(nu) = lambda g(xi) + b(nu_J) + sum_m v_m(R_m nu_J); b(nu_J) = 0; for m != m_0 both omega_m(R_m nu_J) and
  w_m(R_m nu_J) vanish; for m_0: v(R nu_J) = -(lambda/sigma)(omega(z) + c w(z)) = -(lambda/sigma) v(z). []

**Proposition 6.5 (mates at tame f are balanced finite certificates). [PROVED]** Let xi be tame and g in C(f).
Then g = b + sum_m R_m^*(omega_m + c_m w_m) with b supported in F cup K, omega_m supported in Qbar_m (finitely
supported), and the decomposition is unique; moreover v_m(z_m) = 0 for every m and b(xi) = 0. If omega_m is
supported in Q_m, then c_m = -d_m with d_m := <D_m w_m, D_m omega_m>/C_m (the form used in Preprint A).

Proof. Theorem 6.4 gives the form; uniqueness from (F5) (R_m^* injective, Y cap c_00 = {0}, T injective across
blocks). Lemma 6.6 with g(xi) = 0 and Lemma 3.6 (phi(t nu) = o(t^2), nu in ker f) give g(nu) = 0, i.e.
v_{m_0}(z_{m_0}) = 0 for each m_0; then b(xi) = g(xi) - sum_m v_m(z_m) = 0. Finally omega(z) = sigma d
(z_k = sigma Phi_k^2 w_k/C on Q), so v(z) = sigma(d + c) = 0 gives c = -d. []

**Remark 6.7.** The rebalancing direction of Lemma 6.6 moves xi radially in the base and shifts block mass:
at xi + s nu the base norm is (1 + s lambda) q_0 and the m_0-block mass is (1 + s lambda - s lambda/sigma) sigma
(to first order), while the total p** stays 1 + o(s^2). It is a *second-order flat face* of the bidual ball,
parametrising the base/block split. It forces balance (Prop. 6.5) and governs the sharp second-order
coefficient (Section 8). At an NA point x' the same construction works (Theorem 6.2 setting).

**Remark 6.8 (existence of tame non-attaining f). [SKETCH]** Take a in c_00 cap S_{q*}, z in B_{l_inf} with
z_F = sign a_F, |z_j| <= 1/2 off F, z not in c_0; put xi := (z + U e)/p**(z + U e) and f := a + sum_m R_m^* J_m(R_m** xi);
then p*(f) = 1 = f(xi) (decomposition (1.1)) and f is not NA (xi not in c_0, strict convexity). Tameness needs
(T3)-(T4), i.e. |u_{k,m}(xi)| must avoid the windows [0, theta_m Phi_m(k) + o(Phi_m(k))] for all large k. If one
perturbs z by an i.i.d. random sequence on the coordinates off F and the u_{k,m} are not too spread
(e.g. ||u_{k,m}||_2 >= c 2^{-k/3}), Borel-Cantelli gives (T3)-(T4) almost surely. Without information on T,
existence is not proved here. (Preprint A's remark shows that the opposite property, infinitely many
half-peaks, is residual in the bidual face, so tame supports are meagre there.)
