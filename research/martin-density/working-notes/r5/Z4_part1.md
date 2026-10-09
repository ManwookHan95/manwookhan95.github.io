# Z4 part 1: far lowerings — the distance estimate and the band arithmetic

Setting: the note (paper/martin_density_note.tex), Section 8; SLD operator T of Definition def:SLD; N fixed, I = {1..N}, p = p_N.
f in S_{p*} with forced data (xi, q_0, a, w, F, z, zhat, e, nu), F finite. Ladder indices l, carrier (k(l), m(l)), u_l, lambda_l <= c_l/4.
Notation: v_k := m |u_k(zhat)| / |R_m** zhat|_m (block m = m(k)), so the clamp formula (proof of Lemma lem:F1) reads
Phi_k w_m(k) = sign(u_k(zhat)) min(Phi_k M_m, C_m v_k), and C_m is the root of F(c; v) := sum_k min(Phi_k (1-c)/c, v_k)^2 = 1.

## 1.1 Far lowerings f^L (recalled from rem:openZ (O2))
Let L_F be so large that S_l ∩ F = ∅ for l > L_F (F finite, S_l disjoint). For L >= L_F let G_L := union_{l>L} S_l, and let f^L be the first row
with forced data (a, z^L), z^L := 0 on G_L, z^L := z elsewhere (Remark rem:lemmaZ(c)). Then zhat^L - zhat = -z 1_{G_L}, f^L -> f, and
f^L - f = L*(w^L - w) (same base part a).

**Lemma 1.1 (coarse values unchanged).** PROVED. For l <= L: u_l(zhat^L) = u_l(zhat). For l > L: |u_l(zhat^L) - u_l(zhat)| <= ||u_l||_1 <= 1.
*Proof.* supp u_l ⊂ supp y_l ∪ S_l. For l <= L, S_l ∩ G_L = ∅ (disjointness) and supp y_l ∩ S_{l'} = ∅ for l' >= l (allowedness (a)), in
particular for every l' > L. So u_l vanishes on G_L. QED.

## 1.2 The distance estimate (settles the heuristic p*(f^L - f) = O(c_{L+1}))
**Proposition 1.2.** PROVED. Put eps_L := sum_{l>L} lambda_l (<= c_{L+1}/2 by (P2)). There are L_1 and C_f < infinity, depending only on f,
N and the design, such that for L >= L_1:  p*(f^L - f) <= q*(f^L - f) <= C_f eps_L <= C_f c_{L+1}/2.

*Proof.* Fix a block m and drop it. (i) By Lemma 1.1, ||R** zhat^L - R** zhat||_1 = sum_k lambda_k |u_k(zhat^L - zhat)| <= sum_{l>L, m(l)=m} lambda_l
<= eps_L, hence | |R** zhat^L| - |R** zhat| | <= eps_L (|.|_m <= ||.||_1). Let rho_0 := |R** zhat|/2; for L large |R** zhat^L| >= rho_0.
(ii) Increments of v. For carriers l <= L, u_k(zhat^L) = u_k(zhat), so |v^L_k - v_k| = m|u_k(zhat)| | 1/|R**zhat^L| - 1/|R**zhat| |
<= v_k eps_L/rho_0, and the signs of u_k(zhat^L), u_k(zhat) agree. For l > L, |v^L_k - v_k| <= 2m/rho_0. As sum_k Phi_k v_k <= m/(2 rho_0)
(|u_k(zhat)| <= q**(zhat) q*(u_k) = 1 and sum Phi_k <= 1) and sum_{l>L, m(l)=m} Phi_l = sum lambda_l/m <= eps_L/m,
  sum_k Phi_k |v^L_k - v_k| <= eps_L ( m/(2 rho_0^2) + 2/rho_0 ) =: C_1 eps_L.
(iii) C and M. By Proposition prop:continuity (f^L -> f), C^L -> C. The proof of Lemma lem:F1 (root localisation with a fixed peak k_natural
having alpha(k_natural) != 0) applies verbatim with (v, v^L) in place of (v, v'): for L large,
  |C^L - C| = |M^L - M| <= (2(1-C)/(C c_*)) sum_k Phi_k |v^L_k - v_k| <= K_C eps_L,  K_C := 2(1-C) C_1/(C c_*).
(iv) Coordinates. For l <= L the clamp formula with equal signs gives |Phi_k w^L(k) - Phi_k w(k)| <= |C^L - C|(Phi_k + v_k) + C^L |v^L_k - v_k|
<= eps_L ( K_C (Phi_k + v_k) + v_k/rho_0 ) (using min(x,s) Lipschitz in s and |min(Phi(1-c)/c... )| as in Lemma lem:F1; here the clamp level
Phi_k M changes by Phi_k |M^L - M|). Multiply by m (lambda_k = m Phi_k) and sum over k: sum_{l<=L} lambda_k |w^L(k) - w(k)| <= m eps_L (K_C (1 + m/(2rho_0)) + m/(2 rho_0^2)).
For l > L, lambda_l |w^L - w|(k_l) <= 2 lambda_l, summing to <= 2 eps_L.
(v) ||L*(w^L - w)||_1 <= sum_m sum_k lambda_{k,m} |w^L_m(k) - w_m(k)| ||u_{k,m}||_1, and q* <= (1 + ||U||) ||.||_1, p* <= q*. QED.

Remark. The constant C_f depends on f through rho_0, C_m, c_* (a fixed non-degenerate peak), i.e. only on coarse data; eps_L is a design
quantity. So the slack threshold of f^L is t_L(rho) := (6 C_f eps_L/(1-rho^2))^{1/2} = O(c_{L+1}^{1/2}).

## 1.3 The band arithmetic: far lowering gains nothing at inherited scales
**Proposition 1.3.** PROVED. Let g in C(f), rho in (0,1), and t >= A t_L(rho) with A >= 1. Then:
 (a) p*(f^L + tau rho g) <= s(tau) for all |tau| >= t_L(rho) (slack);
 (b) every two-sided decomposition (of g at f, or of rho g at f^L — the latter exists at every scale t >= t_L(rho) by (a) and Lemma lem:twosided,
     whose proof only uses p*(f^L + t rho g) <= s(t)) satisfies sum_{l>L} |Delta theta_l| <= 6 eps_L / t <= t (1 - rho^2)/(C_f A^2);
 (c) for l <= L the swallowing status, the signs eps_l, the values u_l(zhat) and the contact pattern on S_l and on supp y_l are the same at f and f^L.
*Proof.* (a) p*(f^L + tau rho g) <= p*(f + tau rho g) + p*(f^L - f) <= s(rho tau) + C_f eps_L, and s(tau) - s(rho tau) >= (1-rho^2) min(tau^2, |tau|)/3
(Lemma lem:slack(a)); for |tau| >= t_L, (1-rho^2) tau^2/3 >= 2 C_f eps_L. (b) Lemma lem:box: |Delta theta_l| <= 6 lambda_l / t. (c) Lemma 1.1 and
z^L = z off G_L, supp y_l ∩ G_L = ∅ for l <= L. QED.

Consequence (PROVED as stated): on the whole range of scales that f^L inherits from f through the rho-slack, the carriers made roomy by
the lowering carry total switching O(t) (they are negligible exactly like the fine carriers of a window), and the coarse carriers l <= L are
swallowed exactly as at f. Hence a proof that dist(rho g, C(f^L)) -> 0 must, on the band [A t_L, T] of inherited scales, produce exact
data for the FINITELY many swallowed coarse carriers l <= L with constants that the length of the band absorbs: this is the same matching
problem as at f itself with the scale-dependent active set U*(t) ⊂ [1, L] (part 3). Far lowering removes the fine carriers but does not
remove the matching problem; conversely, once the matching is available with absorbable constants, it can be done at f directly (part 3,
Theorem S_Binf), and f^L is not needed. (Heuristic remark: lowering by a factor or on far points of COARSE sets creates room whose pinning
is effective only at scales t^2 <~ lambda_l room_l, while the slack of that lowering covers only t^2 >~ lambda_l room_l — Z1's transition
band; Prop. 1.3 is the rigorous version for whole fine sets.)
