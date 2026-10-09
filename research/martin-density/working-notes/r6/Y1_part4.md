# Y1 part 4 — The exactifying companion f^#_w: closing raises and threshold raises

Setting of part 3 (D_X, f with F finite, clean sub-window w = (l,i), l >= l_f).  Companions keep a (hence e, nu, F): they are
the first rows with forced data (a, z^#), z^# = z on F (Remark rem:lemmaZ(c)), and Delta := zhat^# - zhat = z^# - z.

## 4.1 Donors
**Definition (donor).**  A DONOR of block m is a carrier c = j(k_c, m) such that k_c is a non-degenerate peak of block m
(margin mu_c > 0), S_c ∩ F = {} and vs_c z_s <= 0 for all but finitely many s in S_c (vs_c := sgn w_m(k_c)).
Donors are fixed (f-dependent) carriers; we fix one donor c_m per block that has one, and take l_f >= all c_m.
Examples (PROVED): every exactly swallowed ANTI-TYPE non-degenerate peak (z_s = -vs_c on S_c \ F); at maximal contact (z = eps_0
off F) every block has donors: by Z4 Lemma 5.0 it has non-degenerate peaks with w = -eps_0 M_m (margin >= q_0/4), and their
signature sets are contacts of sign eps_0 = -vs.  A donor is pinned at every window: at w it is either in class R (Lemma 3.5(d))
or in class G with eps_c = -vs_c (the minimizing sign of r^nat_c is -vs_c up to the finitely many exceptional coordinates, which
lie in [1,l] for l >= l_f, so outside S^nat_c), i.e. an anti-type G-peak (Lemma 3.5(a)).  In both cases it is DROPPED.

**Definition (raised blocks).**  Block m NEEDS A RAISE at w if it is not sigma-one-signed at w (Lemma 3.6) and contains a kept
carrier of type (K4) (near-threshold, swallowing type).  Hypothesis (Do_w): every block that needs a raise has a donor.

## 4.2 The companion
**Definition.**  f^# = f^#_w is the companion with z^# := z except:
 (C1) [close rooms] for every class-G carrier l'' <= l: z^#_s := eps_{l''} for s in S^nat_{l''}(l);
 (C2) [close target rooms] for every j in T(l) \ F with 0 < 1 - |z_j| <= b(w): z^#_j := sgn z_j;
 (C3) [raise thresholds] for every block m that needs a raise: let s_m := min(S_{c_m} ∩ (s_max(l), infinity)) (so s_m <= sigma(l),
      s_m notin F ∪ T(l), and vs_{c_m} z_{s_m} <= 0 for l >= l_f) and z^#_{s_m} := z_{s_m} + theta_m vs_{c_m}(1 - vs_{c_m} z_{s_m}),
      theta_m in (0,1] chosen so that lambda_{c_m} |u_{c_m}(Delta)| = T_lo(w)^3 (possible for l >= l_f, see 4.3).
The three sets of modified coordinates are pairwise disjoint (S^nat parts avoid T(l); the S^nat_{l''} lie in distinct signature
sets; s_m notin T(l), and s_m in S_{c_m}; if c_m is in class G, (C3) is applied after (C1)).  |z^#| <= 1 and z^# = z = sgn a on F.

## 4.3 Lemma 4.1 (cost of the companion).  PROVED.
For l >= l_f:  p*(f^#_w - f) <= C_f T_lo(w)^3 log(1/T_lo(w)) =: theta_w T_lo(w)^2,  theta_w := C_f T_lo(w) log(1/T_lo(w)) -> 0,
and ||R_m^*(w^#_m - w_m)||_1 + ||D_m(w^#_m - w_m)||_2 + |C^#_m - C_m| + |M^#_m - M_m| + |sigma^#_m - sigma_m| + |q^#_0 - q_0| <=
C_f T_lo(w)^3 log(1/T_lo(w)).
Proof.  Z3 Lemma 3.1 (any admissible T): p*(f^# - f) <= C_f c(Delta) once max_m Delta_m <= c_f, with Delta_m = sum_k lambda_{k,m}
|u_{k,m}(Delta)| and c(Delta) = sum_m [Delta_m log(e/Delta_m) + sum_k min(lambda_{k,m}, |u_{k,m}(Delta)|)].  Coarse carriers
l'' <= l: (C1) changes u_{l''} only on its own S^nat (no coarse target meets S^nat_{l''}): |u_{l''}(Delta_{C1})| = r^nat_{l''} <= b(w);
(C2) changes every u_{l''} by <= ||u_{l''}||_inf |T(l)| b(w) <= |T(l)| b(w); (C3) changes, among coarse carriers, only u_{c_m}
(s_m notin T(l) and s_m in S_{c_m}), by T_lo(w)^3/lambda_{c_m}.  Fine carriers: sum_{l'>l} min(lambda, .) <= sum lambda <= b(w)^2/2,
and their contribution to Delta_m is <= 2 sum lambda <= b(w)^2.  Hence Delta_m <= l(|T(l)|+1) b(w) + T_lo(w)^3 + b(w)^2 <= 2T_lo(w)^3
(b(w) <= T_lo(w)^4/(l Design(l)) and Design(l) >= 1 + |T(l)|), and c(Delta) <= C N T_lo^3 log(e/T_lo^3) + l(|T|+1) b + sum_m
T_lo^3/lambda_{c_m} + b^2 <= C_f T_lo(w)^3 log(1/T_lo(w)).  The bounds on the block data are those of Z3 Lemma 3.1.
Feasibility of (C3): the available change is lambda_c v_c(s_m)(1 - vs z_{s_m}) >= lambda_c delta_c 2^{-sigma(l)}/n_c, while T_lo(w)^3 <=
T_hi(w)^3 <= Q(w)^{-3} <= Design(l)^{-3} <= 2^{-18 sigma(l)}; so it suffices that 2^{-17 sigma(l)} <= lambda_c delta_c/n_c, true for
l >= l_f since sigma(l) -> infinity (targets have unbounded supports, as they are dense in S_{q*}) and c ranges over N fixed donors.  QED

## 4.4 Lemma 4.2 (data of the companion; status table).  PROVED.
For l >= l_f (l_f larger if necessary, depending only on f) and every coarse carrier l'' <= l other than donors:
 (a) |u_{l''}(zhat^#) - u_{l''}(zhat)| <= (|T(l)| + 1) b(w); and, in zhat-units, ||R_m^** zhat^# - R_m^** zhat||_1 restricted to
     non-donor coordinates is E_m <= 2l(|T(l)|+1) b(w) + b(w)^2.
 (b) In a block m without a raise: |theta^#_m/theta_m - 1| <= C_f E_m (Lemma T2(a)).  In a raised block: theta^#_m/theta_m - 1 =:
     delta_m with c_f T_lo(w)^3 <= delta_m <= C_f T_lo(w)^3 (Lemma T2(b) with s = T_lo(w)^3, E = E_m + b(w)^2 << s; the donor
     stays a peak because its margin is a fixed positive number and the perturbation is <= C_f E_m).
 (c) Relative positions: rho^#_{l''} = rho_{l''} theta_m/theta^#_m + O(C_f D(l)(|T(l)|+1) b(w)).  Hence: robust peaks (rho >= 1+u)
     stay peaks with rho^# >= 1 + u/2; robust strict non-peaks (rho <= 1-u) stay strict non-peaks with rho^# <= 1 - u/2 (gap^# >=
     M^# u/2); nearly neutral carriers keep rho^# <= 2b + C_f D(|T|+1)b; in a RAISED block every near-threshold coordinate
     (|rho - 1| <= b) becomes a strict non-peak with rho^# <= 1 - delta_m/3, i.e. gap^#(k) >= M^#_m delta_m/3 > 0.
 (d) Signature and target structure: class-R carriers keep S^nat_{l''} untouched (rooms unchanged); for a class-G carrier,
     z^# = eps_{l''} on S^nat_{l''}(l) EXACTLY; every j in T(l) \ F is at f^# either a contact (|z^#_j| = 1, with the sign of z_j if
     |z_j| > 0) or a free coordinate with room 1 - |z^#_j| = 1 - |z_j| >= u(w); contacts of f in T(l) keep their sign.
 (e) d-coefficients: for every class-G carrier which is a strict non-peak of f^#, q^#_{l''} = eps u_{l''}(zhat^#)/A^#_m, and
     |q^#_{l''} - q_{l''} A_m/A^#_m| <= (|T(l)|+1) b(w)/A^#_m at strict non-peaks of f (for converted (K4) peaks, |q^#_{l''} -
     Phi M/(m C)| <= C_f(b(w) + delta_m) Phi M/(mC)).  In particular d-neutral carriers (u_{l''}(zhat) = 0) stay EXACTLY d-neutral
     unless their u-vector meets a (C1)-raised set of THEIR OWN S^nat (Lemma 4.3) or a (C2)-raised target coordinate.
Proof.  (a) From the proof of Lemma 4.1 (C3 does not affect non-donor coarse carriers; fine carriers contribute <= b^2 in
l_1(zhat-units)).  (b) Lemma T2 applied to zeta := R_m^** zhat and zeta' := R_m^** zhat^# (all constants of T2 depend on the fixed
vector R_m^** zhat, i.e. on f).  (c) rho = |u(zhat)| m/(Phi theta) (part 2), Phi_{l''} >= 1/D(l), (a), (b); for raised blocks
(1 + b)/(1 + delta) + C_f D(|T|+1) b <= 1 - delta/3 because D(|T|+1)b <= T_lo^4/l << delta; gap^# = M^#(1 - rho^#).  At a clean
sub-window robust means >= u(w) >> delta_m + C_f D(|T|+1) b.  (d) Definitions (C1)-(C3) and the room dichotomy at a clean
sub-window (R2): target rooms are tiny (raised) or >= u(w).  (e) Z6 2.1 at f^# (q = eps u(xi)/sigma = eps u(zhat)/A), (a), and for a
converted peak |u(zhat)| = rho Phi theta/m with |rho - 1| <= b and theta/A = M/C.  QED

## 4.5 Lemma 4.3 (Z3 Lemma 1.4, revisited).  PROVED.
Let l'' be a class-G carrier with r^nat_{l''} > 0 and u_{l''}(zhat) = 0 (d-neutral at f), and suppose no (C2) coordinate meets
supp u_{l''}.  Then eps u_{l''}(zhat^#) = r^nat_{l''} > 0: at f^# it is a strict non-peak with q^# = r^nat/A^#_m > 0, nearly neutral
(rho^# <= C_f D b(w)).  Proof: u(Delta) = sum_{s in S^nat} v(s)(eps - z_s) = eps r^nat by the choice of eps.  QED
So "choose the exactification to keep d-neutrality" is impossible with the same base part (the raise is forced by the closing of
S^nat and its first-order effect has a definite sign: it is the defect Re(u) of Z3), and re-tuning the Hilbert part with supp a
fixed has |F| - 1 degrees of freedom (Z3 referee).  Y4 Proposition 2.8 (unrefereed) shows more: banks of masses at contacts can
only RAISE z-signed functionals (diagonal U), so a positive defect cannot be removed by banks.  In the master theorem (part 5) the
resulting tiny q^# > 0 is HARMLESS in blocks that have a fixed repair direction of negative d-sum (it is compensated by an
O(b(w)/t)-small multiple of that direction), and is the residual item (n) otherwise.
