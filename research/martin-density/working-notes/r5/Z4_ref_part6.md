# Z4 referee, part 6 (addition): rigidity of the d-mismatch for ALL non-d-neutral carriers

## Proposition 5.6' (PROVED; strengthens Z4 Prop 5.6 from peaks to all carriers with w != 0).
Let F be finite and let (b^±, omega^±) be two-piece data at f (Definition def:twopiece) with Delta d_m := d_m(omega^-_m) - d_m(omega^+_m)
!= 0 for some block m. Put Delta := max_{m'} |Delta d_{m'}|, let Omega be the (finite) set of carriers in the supports of the omega^±_{m'},
and T_omega the (finite) union of their target supports. Then for every carrier l of block m with l notin Omega, S_l ∩ F empty and
w_m(k(l)) != 0, every s in S_l with s > max T_omega and 2^{-s} < (2/5)|Delta d_m| |w_m(k(l))| m 2^{-m-k(l)}/(N Delta) is a contact with
  z_s = -sign(Delta d_m) sign(w_m(k(l))).
Equivalently: the far part of S_l is swallowed with a sign eps for which eps Phi w_m(k(l))/(mC_m) (the weight q_l) has sign -sign(Delta d_m).
*Proof.* As in Z4 Prop 5.6, v := b^+ - b^- = sum_{m'} R_{m'}^*(delta omega_{m'} - Delta d_{m'} w_{m'}), delta omega := omega^- - omega^+.
At s as above the delta-omega terms vanish: a carrier k in Omega has u_k(s) != 0 only if s in S_{l(k)} (impossible: l(k) != l and the S are
disjoint) or s in supp y_{l(k)} (impossible: s > max T_omega). For every block m', (R_{m'}^* w_{m'})(s) = [m' = m] lambda_l w_m(k(l)) v_l(s)
+ (targets y_{l'} with s in supp y_{l'}, which forces l' > l by allowedness (a)); by allowedness (b) and lambda_{l'} <= c_{l'}/4,
sum_{l' >= L(s)} c_{l'} <= (4/3) c_{L(s)}, the target part is at most (2/9) 2^{-2s} c_l delta_l in modulus (summed over all blocks), while
|lambda_l w_m(k(l)) v_l(s)| >= (4/5) |w_m(k(l))| m 2^{-m-k(l)} c_l delta_l 2^{-s}. Hence
|v(s) + Delta d_m lambda_l w_m(k(l)) v_l(s)| <= N Delta (2/9) 2^{-2s} c_l delta_l < |Delta d_m lambda_l w_m(k(l)) v_l(s)| by the choice of s,
so v(s) != 0 has the sign -sign(Delta d_m) sign(w_m(k(l))). Two-piece data have v = 0 off F ∪ K and z_j v(j) >= 0 on K; as s notin F,
s is a contact and z_s = sign v(s). QED.
Consequences (PROVED). (a) If block m has infinitely many carriers l with w_m(k(l)) != 0 whose signature sets have infinitely many free
points, or contain contacts of both signs arbitrarily far out, then every set of two-piece data has Delta d_m = 0. (b) Delta d_m > 0
(the option of Corollary cor:D1) requires that all but finitely many non-d-neutral carriers of block m are far-swallowed with q_l < 0;
Delta d_m < 0 (the (SC) regime of Theorem thm:engineered) requires q_l > 0 for all but finitely many of them. (c) Combined with Lemma 3.2 of
the ref notes: under the sign coherence q_l >= 0 the d-identity bounds the two-sided shift from above, and under q_l <= 0 from below; so
sign-coherent swallowing is both the only configuration where non-d-neutral two-piece data can exist and a configuration where one side of
the uniform shift is pinned for free.
