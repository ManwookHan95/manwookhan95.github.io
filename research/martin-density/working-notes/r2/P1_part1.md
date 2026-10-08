# P1 part 1: the certificate span S(f) and the linear obstruction

Setting: canonical base, finite block set I (Martin's p_N; any N >= 1). Notation of A_notes §1, §4.
f in S_{p*}, normer xi, q_0, forced decomposition f = a + L*w, zhat = z + U e, F = supp a,
K = {j notin F : |z_j| = 1} (contacts), for each block m: zeta_m, w_m, M_m, C_m, P_m (peaks),
Q_m = N \ P_m (strict non-peaks), gap_m(k) = M_m - |w_m(k)|, lambda_{k,m} = m Phi_m(k).

## 1.1 Definition (certificate span)
  S(f) := { b + sum_m R_m*(omega_m - d_m(omega_m) w_m) : b in l_1(F), b(zhat) = 0, omega_m in c_00(Q_m) },
  d_m(omega) := <D_m w_m, D_m omega>/C_m.
Equivalently S(f) = (l_1(F) cap zhat^perp) + span{ y_{k,m} : k in Q_m, m in I },
  y_{k,m} := lambda_{k,m} u_{k,m} - (Phi_m(k)^2 w_m(k)/C_m) R_m* w_m.
(Indeed R_m*(e_k - d_m(e_k) w_m) = y_{k,m} and d_m(e_k) = Phi_m(k)^2 w_m(k)/C_m.) Every element h of S(f) has h(xi) = 0.

## 1.2 Lemma (all known recoverable classes lie in cl S(f)). PROVED.
For every f in S_{p*}, each of the following sets is contained in cl S(f) (norm closure in l_1):
 (a) Cert(f) and Cert^sh(f) (A_notes Def 4.1, 4.15): directions g_c, c = (b, omega[, theta]) with supp b in F,
     omega_m in c_00(Q_m) — literally elements of S(f) (||b/a|| < infinity is extra);
 (b) Theorem W directions (A_notes 6.2): b in l_1(F), omega_m off-peak with sum_k lambda_k |omega_m(k)| < infinity:
     limits of truncations, which lie in S(f) (the truncations c_J in the proof of Thm 6.2 are in S(f) and g_{c_J} -> g);
 (c) mates with a locally admissible linear decomposition (Theorem L, A_notes 6.5) and locally split mates
     (D_notes Thm 11.6): by A Lemma 6.3 / D Lemma 11.5, b is supported in F with b(zhat) = 0 and Omega_m = omega_m - d_m w_m
     with omega_m bounded and vanishing on P_m; truncations of omega_m (finite subsets of Q_m) give elements of S(f)
     converging in norm (sum_k lambda_k |omega(k)| <= ||omega||_inf sum_k lambda_k < infinity, and d is continuous);
 (d) the averaging class (A_notes Thm 6.8): it is contained in cl Cert(f);
 (e) C_notes Theorem 7.1 (natural finite certificates): supp b in F, omega_m in c_00(Q_m): in S(f);
 (f) the referee's constant-split two-piece mates (A_referee §5.1): they are finite certificates.
Hence cl Cert^sh(f) and all mates listed in the briefing as "known recoverable at f by intrinsic means" lie in cl S(f).
(The engineered recovery of A_referee §5.4 (SKETCH) is NOT an intrinsic class and is not covered.)

*Proof.* Each item is a direct reading of the definitions/structure lemmas quoted; closures are norm closures and
cl S(f) is a closed subspace. QED.

## 1.3 Corollary (linear obstruction). PROVED.
If g in C(f) and g notin cl S(f), then g lies in the defect Def(f) = C(f) \ cl Cert^sh(f), and more strongly
g is not a norm limit of mates of any of the types (a)-(f).

## 1.4 Remark (when the obstruction can bite)
cl S(f) is a closed subspace of ker(xi) cap l_1. If some block has infinitely many strict non-peaks whose
vectors u_{k,m} are "spread" (e.g. dense in directions of ker xi), then cl S(f) = l_1 cap ker xi and 1.3 is void.
If every Q_m is FINITE ("block-tame" f), then S(f) is finite-dimensional, hence closed, and 1.3 is a finite
linear-algebra test: g notin span{e_j* : j in F} + span{u_{k,m} : k in Q_m} + span{R_m* w_m}.
In particular, at a block-tame f, every mate with a nonzero component on a contact coordinate (in the sense of
not being in that finite span) is in the defect. This is the route to an explicit nonempty defect (part 3).
