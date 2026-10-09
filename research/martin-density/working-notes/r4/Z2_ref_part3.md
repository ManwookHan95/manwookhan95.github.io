# Z2 referee, part 3: contact/cushion structure, routes (b)(i)-(iii), and the open-class bookkeeping

## 1. Prop 4.1 (contact sandwich) and Prop 4.4 (cushions). PROVED, correct (one gloss).
4.1(a): for |z_j| = 1, phi_z(x) = 2(z x)_- and phi_{-z}(x) = 2(z x)_+, so G3 2.3(b) gives sum_K (z B_+)_- <= t/(4q_0), sum_K (z B_-)_+ <= t/(4q_0);
off F cup K, phi >= (1 - |z|)|x|. 4.1(b): B_± = g - L*Omega_± on F^c, so z_j(L*Omega_+)(j) - eps^+_j <= z_j g(j) <= z_j(L*Omega_-)(j) + eps^-_j with
sum(eps^+ + eps^-) <= t/(2q_0). Correct. 4.1(c) repeats the wrong gloss "vanish elsewhere off F up to l_1-mass O(t)" (see part 1, §2): only the
(1 - |z_j|)-weighted mass is O(t) off F cup K.
4.4: for j in F, |a_j + x| - sign(a_j)(a_j + x) = 2(-sign(a_j)x - |a_j|)_+ (re-derived), and the budget gives
sum_F (-sign(a_j)B_+(j) - |a_j|/t)_+ <= t/(4q_0), sum_F (sign(a_j)B_-(j) - |a_j|/t)_+ <= t/(4q_0). Correct for any F (finite or not) and any T.
The reading "two-sided free inside the cushion, contact-like beyond it" is correct AT FIRST ORDER; the Hilbert part (h(B) <= 2/q_0) still constrains
B on F at second order (weakly, U* compact).

## 2. Route (b)(i), Prop 5.1. PROVED as stated; one sentence is HEURISTIC; its scope must be stated.
(a) Construction from (a, z) (G3 referee 3.3) re-checked: q**(z + Ue) <= 1 (z in B_{l_inf}, e in S_H) and a(z + Ue) = ||a||_1 + ||U*a|| = 1, so q**(zhat) = 1;
p**(xi) = q_0(1 + sum_m |R_m** zhat|_m) = 1 = f(xi), p*(f) <= max(q*(a), max_m N_m(w_m)) = 1; R_m** xi != 0 (else xi annihilates a dense subset of S_{q*}).
By uniqueness of the normer (p* smooth) and of the forced decomposition, the base of f is a and its z is the prescribed z. With z_j = sign u(j) on
supp u \ F, phi_{z_j}(c u(j)) = 0 for c >= 0. Correct.
(b), (c): immediate. "each target recurs infinitely often in every block": correct for SLD (G3 Thm A density argument); with z == +1 off F a carrier is
resonant iff y_l >= 0 off F, so infinitely many swallowed carriers are non-resonant. Correct.
HEURISTIC part: "signatures inside supp a give no pinning" is only shown at first order (cushions); no statement that such designs fail is proved.
SCOPE: Prop 5.1 is a statement about FIRST-ORDER BASE COST. It does not say that the corresponding f is outside R (Theorem S, Theorem B± and S3 Cor D2
recover many such f), so "no design removes the bad set" means "no design gives first-order base pinning at every F-finite first row", which is
what 5.1 says. Fine as worded in part 5; the task summary's "design cannot remove swallowing" should carry this qualifier.

## 3. Route (b)(ii), Prop 5.2 (Lemma Z_cert). PROVED, correct.
(=>) C Thm 7.4 (a' in c_00, (f', g') contractive, balanced finite certificate with Gamma_w <= 1; any admissible T; refereed) or S3 Cor D1 (F' finite,
two-piece data, Delta d >= 0, kappa_w <= 1; any admissible T; refereed) give g' in Ls(f'); then (f', rho'g') in cl NA with
||(f', rho'g') - (f, rho' rho g)|| <= p*(f'-f) + p*(g' - rho g) < 2 eps; eps -> 0, rho' -> 1 and A Prop 2.1 give density. (<=, SLD): NA approximants
(f', g') of (f, rho g) with g' in C(f') exist by the rotation argument of G3 Thm C; f' in R_0 and G3 Cor 6.4 (every mate at f' in R_0 is a norm limit
of rho g_c in C(f') with Gamma_w(rho c) <= 1) give (alpha). Correct. (It is a reformulation; its value is that it is design-free and names the target.)

## 4. Route (b)(iii), Prop 5.3. PROVED, correct.
(a) Preprint A Thm "residual uniform recovery" (checked: lsc of f -> dist(z_j, C_d(f)) from upper semicontinuity and global compactness; continuity
points of a lsc function on the Baire space S_{p*} form a dense G_delta; at a continuity point C is lsc; norm-attaining f_n -> f by Bishop-Phelps and
(f_n, G_n) attains at the normer of f_n since G_n vanishes there): Omega ⊂ R, Omega dense G_delta. (b) Preprint A Prop "nonvacuity": {a in c_00} ⊂ U_n F_n,
F_n = [(S_{q*} cap E_n) + L*(B_{V*})] cap S_{p*} compact, hence nowhere dense: {supp a finite} is meagre, so are R_0, R_0^±, R_S, BT, NA cap S. (c) If f' in
A_eps cap R for every eps then (f, rho g) in cl NA (closedness, rho' -> 1); so a non-recoverable (f, rho g) has A_eps ⊂ S \ R ⊂ S \ Omega for small eps.
Correct. Remark: (c) is a sound necessary condition for a counterexample, but it has no bite against the remaining open classes, which are all
contained in the meagre set S \ (Omega ∪ ...) anyway (Z2 says so).

## 5. Open-class bookkeeping: an omission (fixable)
Z2 4.2/4.3/4.5/6 list as OPEN "maximal contact z == sigma off F" and "near-contacts with super-fast room decay". Both lists ignore S3 Cor D2:
EVERY (BT) point (F finite, every Q_m finite, no degenerate peaks, (MS)), WITH ARBITRARY CONTACT SET, is in R for ANY admissible T (refereed). Z2 itself
lists BT ⊂ R in 4.0 and 5.3(a). Hence the open classes are only
  maximal contact / generic infinite non-resonant swallowing / super-fast room decay  AND  NOT (BT)
(i.e. infinitely many strict non-peaks, or degenerate peaks, or failure of (MS)), plus full support without room (F infinite). In particular the
"model obstruction" of 4.2 (uncontrolled Hoffman constants for infinitely many swallowed non-resonant carriers) is an obstruction to the method of
Theorem S, not to recovery: at maximal-contact (BT) points, S3's Fenchel-duality theorem produces optimal two-piece data directly (no pinning needed).
Conversely, Theorem S and Theorem B± are genuinely new exactly where (BT) fails (infinitely many strict non-peaks, degenerate peaks other than (H5),
failure of (MS)). The status table should say so.
Also: under (S_inf), Theorem S's hypotheses force infinitely many d-neutral (u_l(xi) = 0) strict non-peaks, so R_S \ BT is non-trivial there; under
(S_fin), R_S \ BT is non-empty only if f fails (BT) for reasons unrelated to B (Q_m infinite, degenerate good peaks, or (MS) failing) — which is
allowed, so the theorem is not vacuous, but its novelty over S3 D2 is the block side, not the contact side.
