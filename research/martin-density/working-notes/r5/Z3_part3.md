# Z3 part 3 — transplanting window decompositions to exactifying companions (SLD operator)

T = operator of Definition def:SLD, N >= 1, I = {1..N}, p = p_N; f in S_{p*} with F finite, g in C(f).
A *coarse exactification* of f for a window index l_* is a companion f^# (part 1) with
   z^# := eps_l on S_l \ F for l in A,   z^# := z elsewhere,   delta := z^# - z,
where A is a finite set of coarse ladder indices (l <= l_*) such that z is NOT identically eps_l on S_l \ F (approximately swallowed
carriers; their rooms r_l at f may be positive). On supp delta, delta_j = eps_l - z_j: a *raise* if sgn z_j = eps_l (|delta_j| = 1-|z_j|),
a *flip* if z_j = -eps_l (|delta_j| = 2), otherwise a move of size <= 1 + |z_j|.

## 3.1 Lemma (cost of a companion). PROVED.
Put Delta_m := ||R_m^** delta||_1 = sum_k lambda_{k,m} |u_{k,m}(delta)| and
   c(delta) := sum_m [ Delta_m log(e/Delta_m) + sum_k min(lambda_{k,m}, |u_{k,m}(delta)|) ].
There are c_f, C_f (depending only on f, N, T) such that if max_m Delta_m <= c_f then
   |C^#_m - C_m| + |sigma^#_m - sigma_m| + |q^#_0 - q_0| <= C_f max_m Delta_m,
   sum_m ||R_m^*(w^#_m - w_m)||_1 <= C_f c(delta),   ||D_m(w^#_m - w_m)||_2^2 <= C_f c(delta)^2,
   p*(f^# - f) <= (1 + ||U||) C_f c(delta).
(A priori closeness: zeta^#_m = q^#_0 R_m^** zhat^# is l_1-close to (q^#_0/q_0) zeta_m when Delta is small, J_m is norm-to-weak*
continuous at zeta_m != 0 (smoothness of |.|_m) and D_m is weak*-to-norm continuous on bounded sets; so C^#_m -> C_m, M^#_m -> M_m as
max_m Delta_m -> 0, which is what "Delta below c_f" provides.)
*Proof.* Fix m, drop it; v_k := m|u_k(zhat)|/|R^**zhat|, v^#_k likewise. Clamp formula (proof of Lemma lem:F1): Phi_k w(k) =
sgn(u_k(zhat)) min(Phi_k M, C v_k), and C is the root in (0,1) of sum_k min(Phi_k(1-c)/c, v_k)^2 = 1. As |R^**zhat^#| - |R^**zhat|| <= Delta
and |u_k(zhat)| <= 1 + ||U||: |v^#_k - v_k| <= c_1(|u_k(delta)| + Delta) with c_1 depending on f. The proof of Lemma lem:F1 (strict decrease
of F(.; v) near C through a peak with alpha != 0; |min(x,s)^2 - min(x,s')^2| <= 2x|s - s'|) gives, once Delta is below a constant c_f
ensuring |C^# - C| <= r and |v^#_{k_nat} - v_{k_nat}| <= r, |C^# - C| <= c_2 sum_k Phi_k |v^#_k - v_k| <= c_3 Delta (sum_k Phi_k <= 1,
sum_k Phi_k |u_k(delta)| <= Delta/m). q_0 = (1 + sum_m |R_m^** zhat|)^{-1} and sigma_m = q_0|R_m^** zhat| move by O(Delta). For each k, as
in Lemma lem:F1, Phi_k|w^#(k) - w(k)| <= |C^#-C|(Phi_k + v_k) + C^#|v^#_k - v_k| (same signs or one vanishes) and <= C^#v^#_k + C v_k <=
c_4|u_k(delta)| (opposite signs: then both |u_k(zhat)|, |u_k(zhat^#)| <= |u_k(delta)|). With lambda_k = m Phi_k, |w|, |w^#| <= 1 and
min(a, x+y+z) <= x + min(a,y) + min(a,z):
   lambda_k|w^#(k) - w(k)| <= m|C^#-C| Phi_k + min(2 lambda_k, c_5 Delta) + min(2 lambda_k, c_5 |u_k(delta)|).
Sum over k: sum_k min(2 lambda_k, x) <= x(log_2(2m/x) + 3) for lambda_k <= m 2^{-m-k} (count the k with lambda_k > x/2, and sum the
geometric tail). This gives the l_1 bound. For the D-bound: ||D(w^# - w)||^2 <= max_k Phi_k|w^#(k) - w(k)| * sum_k Phi_k|w^#(k)-w(k)|;
the second factor is (1/m) sum_k lambda_k |w^#(k) - w(k)| <= C c(delta), and by the two pointwise bounds above together with
Phi_k|w^#(k) - w(k)| <= 2 Phi_k, the first factor is <= c_6 Delta + min(2 Phi_k, c_6 |u_k(delta)|) <= c_7 c(delta) (each term of c(delta)
dominates the corresponding quantity). Finally f^# - f = L^*(w^# - w) and p* <= q* <= (1+||U||)||.||_1 on X*. QED

## 3.2 Lemma (budget of the actual decomposition at the companion). PROVED.
Let (B_+-, Theta_+-) be a two-sided decomposition of g at f at scale t. Then
   sum_{j notin F} phi_{z^#_j}(B_+(j)) <= t/q_0 + 2 sum_{j flipped} |B_+(j)|,
and the same for phi_{-z^#_j}(B_-(j)). On raised coordinates phi_{z^#_j}(x) <= 2 phi_{z_j}(x); on flipped ones phi_{z^#_j}(x) <= 2|x|.
*Proof.* Raised j (z^#_j = sgn z_j, |z_j| < 1): if sgn x = sgn z_j, phi_{z^#}(x) = 0; otherwise phi_{z^#}(x) = 2|x| <= 2(1+|z_j|)|x|/(1+|z_j|)
= 2 phi_{z_j}(x)/(1+|z_j|). Flipped: phi_{-z}(x) = |x| + zx <= 2|x|. Elsewhere phi_{z^#} = phi_z. Lemma lem:switchbudget. QED

## 3.3 Proposition T (transplant). PROVED (by the indicated modifications of Lemmas lem:modswallow-lem:windowtwopiece).
Let l_* be a window index and f^# a coarse exactification of f with set A. Let B be the set of exactly swallowed carriers of f, assume
B is finite with max B <= l_*, and put B' := A u B. Assume, with constants independent of the scale t in W(l_*):
 (P) [pinning at f] r*_l > 0 for good l notin B', where r*_l is computed at f with B' in place of B (Definition def:swallowed), (H1) for
     B' (targets of l' in B' do not meet S_l for l < l', l, l' in B'), and at f the conditions (H2) and (H3) hold for B'
     (the swallowing signs of l in A are the eps_l above). Put K_* := (1/q_0 + 22) Lambda*_{f,B'}(l_*).
 (BS) [block stability] Delta := max_m Delta_m <= c_f and c(delta) + Delta <= theta T_lo(l_*)^2 for a theta <= 1; every coarse k
     (j(k,m) <= l_*) has the same status at f and f^# (peak with the same sign / strict non-peak), and every k(l), l in B', that is a
     strict non-peak at f has gap^#(k(l)) >= gamma_B > 0.
 (HF) [Hoffman] the polyhedron Z^# defined at f^# by the conditions of Lemma lem:exactswitch for B' (tau_l >= 0; z^#-signs on T_0 cap K^#;
     vanishing on T_0 \ (F u K^#); tau_l = 0 at peaks; sum_{m(l)=m} q^#_l tau_l = 0 for every m), together with the box rows
     tau_l <= 6 lambda_l/t, has Hoffman constant <= C_H^# (Hoffman constants do not depend on the right sides).
Then for every t in W(l_*) with t <= min(t_eta, 1) and (C_H^# + 1) K_* t <= 1, g has a functional g_t carrying d-neutral two-piece data
AT f^# satisfying (E-a), (E-b) of Theorem E with A_0, A_2 = 10 and gamma_B independent of t, and
     p*(g - g_t) <= C (1 + C_H^#)(K_* + theta) t ,   Gamma^#_w(b^+-, omega^+-) <= (sqrt(1+eta_Gamma(eta)) + C(1 + C_H^#)(K_* + theta) t)^2,
where C depends only on f, N, gamma_B and the design.
*Proof (the changes w.r.t. the proofs of Lemmas lem:modswallow, lem:badpeaks, lem:exactswitch, lem:windowtwopiece).*
(1) Pinning at f modulo B'. The proof of Lemma lem:modswallow uses only that the right sides of the good inequalities contain good later
indices; with B' in place of B it gives sum_{l notin B'} |Delta theta_l| <= K_* t and, for l in B', the bad inequality
(tau_l)_- <= (E_l + ...)/r*_l with r*_l >= (2 - max(1-|z|))||v_l 1_{S_l \ F}||-type constant (on S_l \ F, phi_{z_s}(-Delta theta_l v_l(s))
>= (1 + eps_l z_s)(tau_l)_- v_l(s) and 1 + eps_l z_s is bounded below on the part of S_l \ F where z is close to eps_l, which carries all but
the room of the v_l-mass). Lemma lem:badpeaks holds verbatim at f for B' ((H2), (H3) for B').
(2) Violations at f^#. With L(tau) := sum_{l in B'} eps_l tau_l u_l and the actual amplitudes tau, ||Delta B 1_{F^c} - L(tau)1_{F^c}||_1 <=
K_* t + 6t^2. Cost at f^#: by Lemma 3.2 and Lemma lem:phicalc(c), c^#(tau) := sum_{j notin F} phi_{z^#_j}(L_j(tau)) <= 2t/q_0 + 2 S_fl + C K_* t,
S_fl := sum_{flipped j} |Delta B(j)|; on a flipped j in S_l, Delta B(j) = eps_l tau_l v_l(j) + O(pinned), and phi_{z_j}(eps_l tau_l v_l(j)) =
2(tau_l)_+ v_l(j) is part of the budget at f, while (tau_l)_- is bounded by (1); so S_fl <= C K_* t. Peaks: as in Lemma lem:exactswitch,
|tau_l| <= C lambda_l t at non-degenerate bad peaks and tau_l <= lambda_l K_d t at degenerate bad peaks of sign -eps_l ((BS): same peaks at
f^#). d-conditions at f^#: by Lemma 1.2(b) and 1.3, for every m,
   |R_m^** zhat^#| sum_{m(l)=m, k(l) in Q} q^#_l tau_l - |R_m^** zhat| sum_{m(l)=m, k(l) in Q} q_l tau_l = V_m(delta),
V_m := sum_{m(l)=m, k(l) in Q} eps_l tau_l u_l; by (H1) for B' the signature coordinates of supp delta carry only their own carrier, so
|V_m(delta)| <= sum_{raised} (1-|z_j|)|V_m(j)| + 2 sum_{flipped}|V_m(j)| + C K_* t <= C(t + K_* t) (Lemma 1.1(c) and the bound on S_fl), while
|sum q_l tau_l| <= C K_* t by Lemma lem:badpeaks(b) at f. The box rows hold exactly (Lemma lem:box). Hence the total violation of the
rows of (HF) by tau is <= C K_* t.
(3) Projection. Hoffman gives tau' in Z^# with tau'_l <= 6 lambda_l/t and sum |tau_l - tau'_l| <= C C_H^# K_* t; V' := L(tau')1_{F^c} is
z^#-signed and supported in K^#, and ||Delta B 1_{F^c} - V'||_1 <= C(1 + C_H^#) K_* t.
(4) Split and data. Lemma lem:split holds with z^# in place of z, its proof using only phi_{z^#_j}(B_+(j)) + phi_{-z^#_j}(B_-(j)) summed
(Lemma 3.2: <= 2t/q_0 + C K_* t) and V' z^#-signed in K^#: B_+ 1_{F^c} = chi V' + e_+, B_- 1_{F^c} = -(1-chi)V' + e_- with ||e_+-||_1 <=
C(1 + C_H^#)K_* t. Define the data exactly as in Lemma lem:windowtwopiece but AT f^#: omega^+_m := clamp of omega_{+,m} at the coarse
strict non-peaks with the gaps of f^# (Definition def:windowcert with gap^#), and omega^+_m(k(l)) := omega_{+,m}(k(l)) at the switching
non-peaks; omega^- := omega^+ + sum (eps_l tau'_l/lambda_l) e_{k(l)}; b^+ := B_+ 1_F + chi V' - kappa^# a with kappa^# := (B_+1_F + chi V')(zhat^#);
b^- := b^+ - sum eps_l tau'_l u_l; g_t := b^+ + sum_m R_m^*(omega^+_m - d^#_m(omega^+_m) w^#_m). Two-piece admissibility at f^#, the second
representation and Delta d^# = sum q^#_l tau'_l = 0 are verified as in Lemma lem:windowtwopiece(a).
(5) Estimates. kappa^# = B_+(zhat^#) - (e_+)(zhat^#) - ... and B_+(zhat^#) = B_+(zhat) + B_+(delta), |B_+(zhat)| <= t/(2q_0), |B_+(delta)| <=
sum_{raised}(1-|z_j|)|B_+(j)| + 2 sum_{flipped}|B_+(j)| <= C K_* t; hence |kappa^#| <= C(1+C_H^#)K_* t. The comparison of g_t with
g = B_+ + sum R_m^* Theta_{+,m} is that of Lemma lem:windowtwopiece(b) plus the terms coming from replacing (d, w, gap) by (d^#, w^#, gap^#):
 * sum_m R_m^*(d^#_m(omega^+)w^#_m - d_m(omega^+)w_m) = sum d^#(w^# - w)-terms + (d^# - d)w-terms; |d^#_m(omega^+)| <= 4/t ((d) of Lemma
   lem:windowtwopiece), ||R^*(w^# - w)||_1 <= C_f c(delta) <= C theta t^2 (Lemma 3.1, (BS)); by Lemma 1.2(b), |d^# - d|(omega^+) <=
   (|(R^*omega^+)(delta)| + |d(omega^+)| Delta)/|R^** zhat^#| with |(R^*omega^+)(delta)| <= ||omega^+||_inf Delta <= (10/t) theta t^2;
 * re-clamping with gap^# instead of gap changes omega^+ by at most 2|gap^#(k) - gap(k)|/t <= 2(|w^#(k) - w(k)| + |M^# - M|)/t at coarse
   k, whose lambda-weighted sum is <= C theta t;
 * status is unchanged at coarse k by (BS).
So p*(g - g_t) <= (1+||U||)||g - g_t||_1 <= C(1+C_H^#)(K_* + theta)t. For Gamma^#_w: sqrt(Gamma^#_w) is a seminorm; compare the + data with
(B_+, Theta_+) and the - data with (B_-, Theta_-) as in Lemma lem:windowtwopiece(c), and use Gamma^#_w(B_+-, Theta_+-) <=
Gamma_w(B_+-, Theta_+-) + C(||D(w^# - w)|| + |C^# - C| + |q^#_0 - q_0| + |sigma^# - sigma|)(1 + ||D Theta_+-||)^2 with ||D Theta_+-|| <= 4/t
(box) and ||D(w^#-w)|| + Delta <= C sqrt(theta) t (Lemma 3.1, (BS)): the P^perp-projections onto (D w^#)^perp and (D w)^perp differ in
operator norm by <= 2||D(w^# - w)||/C + 2|C^# - C|/C. Size conditions (E-b): coarse coordinates as in Lemma lem:windowtwopiece(d) with
gap^#; switching coordinates: |omega^+(k(l))| <= 4/t and |omega^-(k(l))| <= 4/t + tau'_l/lambda_l <= 10/t (box rows), gap^# >= gamma_B by (BS).
t||b^+-||_1 <= A_0 as in Lemma lem:windowtwopiece(d). QED

## 3.4 Corollary (exactification windows). PROVED (Theorem E + Proposition T).
If there are window indices l_1 < l_2 < ... and coarse exactifications f^#_j for W(l_j) satisfying (P), (BS) with theta_j -> 0
(T_lo := T_lo(l_j), the bottom of the design window, whose n^w_{l_j} dyadic scales are all used), and (HF) with
   (1 + C^#_{H,j}) K_{*,j} T_hi(l_j) -> 0  and  n^w_{l_j} / ((1 + C^#_{H,j}) K_{*,j}) -> infinity,
with gamma_B uniform, then f in Rec. (Here (E-e) follows from (BS) and Lemma 3.1: p*(f^#_j - f) <= C c(delta_j) <= C theta_j T_lo(l_j)^2;
in (E-c), K_j := C(1 + C^#_{H,j})(K_{*,j} + 1).) In particular every first row with F finite in which the approximately swallowed
carriers can be exactified window by window at cost c(delta_j) = o(T_lo(l_j)^2), with good companion cones and with the remaining
coarse carriers pinned within the window budget, is recoverable.
