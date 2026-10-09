# Z3 part 1 — structural facts about first-order defects (any admissible T unless stated)

Notation of the note (paper/martin_density_note.tex). I finite, f in S_{p*} with forced data (xi, q_0, a, w, F, z, zhat, e, nu),
phi_z(x) := |x| - z x. A *companion* of f is a first row f^# with the SAME base part a and contact data z^# in B_{l_inf} with
z^# = z on F (= sgn a); it exists and is unique by Remark rem:lemmaZ(c) (data (a, z^#), e^# = e), and zhat^# = zhat + delta with
delta := z^# - z supported in F^c. Data of f^# carry the superscript #.

## 1.1 Lemma (scale-dependent effective contact set). PROVED.
Let (B_+-, Theta_+-) be a two-sided decomposition of g in C(f) at scale t > 0 (Lemma lem:twosided), F arbitrary. For theta in (0,1] put
N_theta := {j notin F : 1 - |z_j| <= theta} (contains K). Then
 (a) sum_{j notin F, j notin N_theta} |B_+-(j)| <= t/(2 theta q_0);
 (b) for theta < 1: sum_{j in N_theta} (sgn(z_j) B_+(j))_- <= t/(2(2-theta) q_0) and sum_{j in N_theta} (sgn(z_j) B_-(j))_+ <= t/(2(2-theta) q_0);
 (c) sum_{j in N_theta} (1 - |z_j|) |B_+-(j)| <= t/(2 q_0).
*Proof.* Lemma lem:switchbudget: sum_{j notin F} phi_{z_j}(B_+(j)) <= t/(2q_0), sum phi_{-z_j}(B_-(j)) <= t/(2q_0). Off N_theta,
phi_{+-z_j}(x) >= (1-|z_j|)|x| > theta|x|: (a). On N_theta (theta < 1, so z_j != 0), if sgn(z_j) x < 0 then phi_{z_j}(x) = (1+|z_j|)|x| >= (2-theta)|x|:
(b) (for B_- use phi_{-z_j}). (c): phi_{+-z_j}(x) >= (1-|z_j|)|x|. QED
*Meaning.* At scale t the switching can use, at bounded first-order cost, only coordinates of room <~ t/(mass): the effective contact set
K u N_theta shrinks to K as t -> 0. Approximate swallowing = switching on N_theta \ K with (1-|z|)-weighted mass O(t) (part (c)) but
l_1-mass not O(t) (Remark rem:budgetgloss). Wrong-signed mass on N_theta is always O(t) in l_1 (part (b)).

## 1.2 Lemma (d-coefficients through the normer; defect identity). PROVED.
(a) For every block m and omega in c_00(Q_m): d_m(omega) = (R_m^* omega)(zhat) / |R_m^** zhat|_m.
(b) If f^# is a companion and omega in c_00(Q_m cap Q^#_m), then
      |R_m^** zhat^#|_m d^#_m(omega) - |R_m^** zhat|_m d_m(omega) = (R_m^* omega)(delta).
*Proof.* (a) Lemma lem:threshold for zeta_m = R_m^** xi = q_0 R_m^** zhat: off P_m, Phi_m(k)^2 w_m(k)/C_m = zeta_m(k)/sigma_m. Hence
d_m(omega) = sum_k Phi_m(k)^2 w_m(k) omega(k)/C_m = <omega, zeta_m>/sigma_m = <omega, R_m^** zhat>/|R_m^** zhat|_m, and <omega, R_m^** theta> =
(R_m^* omega)(theta). (b) Apply (a) at f and at f^# and subtract; zhat^# - zhat = delta. QED

## 1.3 Corollary (raising converts a first-order defect into a d-mismatch). PROVED.
Let V := sum_l eps_l tau_l u_l (carriers k(l) in block m, strict non-peaks of f and of f^#), i.e. V = R_m^*(omega^- - omega^+) for the
switching omega^- - omega^+ := sum_l (eps_l tau_l / lambda_l) e_{k(l)}. If z^#_j in {+-1} and z^#_j V_j >= 0 for every j in supp delta, then
      |R_m^** zhat^#|_m Delta d^#_m - |R_m^** zhat|_m Delta d_m = V(delta) = sum_{j in supp delta} phi_{z_j}(V_j) >= 0,
where Delta d := d(omega^-) - d(omega^+). In words: if the switching is d-neutral at f, then at a companion which makes its near-contacts
(or wrong-signed contacts) exact contacts with the switching sign, it has d-mismatch EXACTLY equal to its first-order defect on the
modified coordinates divided by |R_m^** zhat^#|_m; in particular >= 0.
*Proof.* Lemma 1.2(b) with omega = omega^- - omega^+ and R_m^* e_{k} = lambda_{k,m} u_{k,m}. For j in supp delta, V_j delta_j = V_j(z^#_j - z_j) =
|V_j| - z_j V_j = phi_{z_j}(V_j) because z^#_j = sgn V_j when V_j != 0. QED
*Size.* For the projected window switching (Lemma lem:exactswitch, Lemma lem:split), V = Delta B 1_{F^c} up to l_1-error O(K t), so by
Lemma 1.1 and Lemma lem:phicalc(c) the right side is <= t/q_0 + O(K t): the d-mismatch created at a companion is O(K t)/sigma-scale.

## 1.4 Lemma (approximate resonance and d-neutrality are incompatible at companions). PROVED.
Let u in l_1, eps in {+-1}, and let f^# be a companion of f such that eps u_j z^#_j = |u_j| for all j in supp u \ F (eps u 1_{F^c} is
z^#-signed and supported in K^#). Then
      eps u(zhat^#) - eps u(zhat) = Re(u) := sum_{j notin F} phi_{z_j}(eps u_j) >= 0.
Consequently, if the carrier k = k(l) (u = u_l, eps = eps_l) is d-neutral at f (w_m(k) = 0, equivalently u(zhat) = 0) and its switching
direction has positive first-order defect Re(u_l) > 0 at f, then at EVERY companion at which it is exactly resonant and a strict
non-peak, w^#_m(k) = C^#_m m eps_l Re(u_l) / (Phi_m(k) |R_m^** zhat^#|_m) != 0: it is not d-neutral there, and its weight
q^#_l := eps_l Phi_m(k) w^#_m(k)/(m C^#_m) = Re(u_l)/|R_m^** zhat^#|_m > 0.
*Proof.* zhat^# - zhat = delta vanishes on F, and the U-parts coincide (same e). So eps u(zhat^#) - eps u(zhat) = sum_{F^c} eps u_j (z^#_j - z_j)
= sum_{F^c} (|u_j| - eps u_j z_j) = Re(u). For the second statement use Lemma lem:threshold at f^# (strict non-peak):
w^#_m(k) = C^#_m zeta^#_m(k)/(Phi^2 sigma^#_m) with zeta^#_m(k) = q^#_0 lambda_k u(zhat^#) and sigma^#_m = q^#_0 |R_m^** zhat^#|_m. QED
*Consequence for the method of Theorem thm:S at companions (PROVED).* If all switching carriers of a block are of this kind, every
q^#_l > 0 and the cone of exact d-neutral resonances at f^# (Lemma lem:exactswitch) meets {tau >= 0} only in 0: the Hoffman projection
at f^# then costs the whole switching, not O(K t). Exactness at a companion with the same base part therefore requires either
carriers of both signs of q^# in the block, or a re-tuning of the Hilbert part (moving a, hence e) — see part 4.

## 1.5 Remark (why fixed-defect data fail; the kink). PROVED (as a statement about the bounds), not a non-recovery claim.
(a) At f, a side-+ pair (b, omega) representing g with b(xi) = 0, omega in c_00(Q) and b supported in F u K u N gives, for 0 < r small,
p*(f + r g) <= 1 + q_0 r D^+(b) + (r^2/2)(Gamma_w(b,omega) + o(1)), D^+(b) := sum_{j notin F} phi_{z_j}(b_j)  (proof of Prop
prop:onesidedupper: the only change is Exc(r b) = r D^+(b) instead of 0, which enters the weighted excess Gamma-hat with weight q_0).
The term q_0 r D^+ is first order: such data certify NOTHING at scales r << q_0 D^+.
(b) At window scale t the defect of the projected window data is D^+ <= t/(2q_0) + O(K t) (Lemma 1.1), i.e. of the size of the whole
quadratic budget at scale t. Hence the one-sided transfer expansion (Lemma lem:onesidedtransfer: |r| <= c_flat t) fails for such data,
and in the windowed averaging at f (Theorem thm:windowed, Lemma lem:avgfunctionals) every coarse-scale piece t_i >> r contributes the
first-order term rho|r| q_0 D_i <= rho|r| t_i/2: the average carries a kink of slope ~ T_hi/n. This is the "exactness versus scale"
tension of Remark rem:openZ in quantitative form: no averaging AT f of defect data can produce a mate below scale ~ T_hi/n.
(c) In Theorem thm:engineered with FIXED data, a first-order defect enters Step 3 (base) as rho|tau| D (or, if the near-contacts are
raised in f', as a level shift rho|tau|E_v/2 removed by rebalancing at cost ~ iota |tau| E_v). Either way it is admissible only if it is
<= c delta s_1 with an admissible s_1 <~ T_0^2 (SKETCH: s_1 need not tend to 0; the construction with s_1 fixed and N_w, N'' -> infinity
converges to a companion-type first row, and all "o(s_1)" terms become s_1 * o_{s_1 -> 0}(1)). So fixed data tolerate only defects
below a positive threshold ~ T_0^2(data); window data have defect ~ T_hi/n >> T_0^2 ~ (n T_lo)^2. An "approximately two-piece Cor D1"
with defects proportional to the scale of the data is therefore NOT available at f; defects must be removed by changing the first row.
