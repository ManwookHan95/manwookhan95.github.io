# Z3 referee, part 1 — Z3 parts 1-2 (first-order defects; Lemma U; Theorem E)

Reference: paper/martin_density_note.tex (numbering and notation). I finite, p = p_N. Each item: verdict, then the line-by-line check.

## 1.1 Lemma 1.1 (effective contact set). CORRECT.
Re-derived from Lemma lem:switchbudget (valid for every t > 0: its proof uses only Lemma lem:bookkeeping(a), g(xi) = 0,
s(t) - 1 <= t^2/2 and nonnegativity of the block excesses). Off N_theta: phi_{+-z_j}(x) >= (1 - |z_j|)|x| > theta|x|, so the l_1-mass of
EACH of B_+, B_- there is <= t/(2 theta q_0) (for Delta B: t/(theta q_0)). On N_theta with theta < 1 one has |z_j| >= 1 - theta > 0 and, if
sgn(z_j)x < 0, phi_{z_j}(x) = (1 + |z_j|)|x| >= (2 - theta)|x|; symmetrically for B_- with phi_{-z_j}. (c) is phi >= (1 - |z|)|x|.
Remark: theta < 1 is needed in (b) (at theta = 1, N_1 contains coordinates with z_j = 0, which have no sign); the note's statement
respects this.

## 1.2 Lemma 1.2 (d through the normer; defect identity). CORRECT.
(a) Lemma lem:threshold off P_m: Phi_m(k)^2 w_m(k)/C_m = zeta_m(k)/sigma_m; summing against omega in c_00(Q_m) gives
d_m(omega) = <omega, zeta_m>/sigma_m, and zeta_m = q_0 R_m^** zhat, sigma_m = q_0|R_m^** zhat|_m, <omega, R^** theta> = (R^* omega)(theta).
(b) A companion has the same a, hence the same e and nu, and z^# = z on F; so zhat^# - zhat = z^# - z = delta (supported in F^c) and
(a) at both points, for omega in c_00(Q_m cap Q^#_m), subtracts to the identity. Numerically confirmed (Z3_ref_work/check_dnormer.py,
150 random blocks and companions: (a) max relative error 3e-17, (b) 2e-12, i.e. bisection precision).

## 1.3 Corollary 1.3 (raising converts defect into d-mismatch). CORRECT, with one precision.
Lemma 1.2(b) with omega = omega^- - omega^+ (d is linear) and R_m^* e_k = lambda_k u_k. On supp delta with z^#_j = sgn V_j (V_j != 0):
V_j delta_j = |V_j| - z_j V_j = phi_{z_j}(V_j). Precision: only the defect ON supp delta is converted; the identity says nothing about the
defect of V on coordinates that are not moved.
IMPORTANT consequence that the notes state only implicitly (and that I verified): the nonnegative d-mismatch produced at the companion
can NOT be fed to Corollary cor:D1 (which tolerates Delta d_m >= 0) through finitely supported two-piece data: two representations of
one functional force b^+ - b^- = R_m^*(omega^- - omega^+) - Delta d_m R_m^* w^#_m, and R_m^* w^#_m has infinitely many peak terms, so its
restriction to F^c is not supported in K^# u F unless Delta d_m = 0 (Lemma lem:rigidity(b)-type independence). This is Remark rem:S(b)
of the note; it is the reason why Lemma 1.4 matters.

## 1.4 Lemma 1.4 (approximate resonance vs d-neutrality). CORRECT; the Hoffman-constant gloss is HEURISTIC in its constant.
eps u(zhat^#) - eps u(zhat) = sum_{F^c} eps u_j (z^#_j - z_j) = sum (|u_j| - eps u_j z_j) = Re(u): checked. d-neutral at f <=> w_m(k) = 0 <=>
u_k(zhat) = 0 (a zero zeta_m(k) cannot sit on P_m, since alpha would get the sign opposite to w; and w(k) = 0 forces k notin P_m). At a
strict non-peak of f^#: w^#(k) = C^# m u(zhat^#)/(Phi_k |R^** zhat^#|) and q^#_l = eps Phi w^#/(m C^#) = Re(u_l)/|R^** zhat^#|: checked.
Cone consequence: if every switching carrier of a block has q^# > 0, {tau >= 0, sum q^# tau = 0} = {0}: correct.
"Hoffman constant >~ 1/room": the correct lower bound is C_H^# >= |R^** zhat^#|_m / min_l Re(u_l) (test tau = e_l). Since Re(u_l) =
(signature room r_l) + (target part) >= r_l, this is >~ 1/r_l only when the target part of Re is comparable to r_l. As a statement about
the method (the companion buys nothing over pinning when Re ~ r_l) it is right; the constant claim should read 1/Re(u_l).

## 1.5 Remark 1.5 (kink). (a), (b) CORRECT as statements about the available bounds; (c) SKETCH (labelled so) — plausible.
(a) In the proof of Proposition prop:onesidedupper the only change is Exc(tb) = t D^+(b); it enters Gamma-hat with weight q_0, and
through epsilon_m = (G_m - Gamma-hat)/e_y it also enters the rebalancing error with a factor O(eta_1). So the correct bound is
p*(f + r g) <= 1 + q_0 r D^+ (1 + O(eta_1)) + (r^2/2)(Gamma_w + o(1)); harmless. This is an UPPER bound: it shows the data certify
nothing below scale ~D, not that g is not certified by other data (the notes say so).
(b) D_i <= t_i/(2q_0) + O(K t_i) is an upper bound; "the average carries a kink of slope ~T_hi/n" is a statement about the bound
(the actual defects may be smaller). Fine as labelled.
(c) In Theorem thm:engineered a first-order base defect D enters Step 3 as rho|tau|D and is affordable for |tau| > s_1 iff D <~ delta s_1;
for |tau| <= s_1 the theta-data are used, whose base part lives on window contacts WITH mass (exact). Defect data at near-contacts
(|z_j| < 1) cannot receive window masses without raising z_j (z' = sgn a' on supp a'), so either the defect stays (needs D <~ s_1) or
the near-contacts are raised (a companion-type move whose p*-cost must be <~ T_0^2 by Lemma lem:assembly). With s_1 fixed and
N_w, N'' -> infinity the approximants converge to a first row at distance ~ s_1 ||b^theta||_1 from f, and Lemma lem:assembly needs
p*(f' - f) <= (1 - rho^2) T_0^2/6; hence the threshold ~T_0^2. Plausible SKETCH; not needed elsewhere.

## 1.6 Lemma U (uniform one-sided transfer expansion along f_j -> f, supp a_j = F). CORRECT.
I re-traced every constant in the proofs of Lemmas lem:uniformtransfer and lem:onesidedtransfer:
* base: c_flat A_0 <= a_min (no flips), ||r U^* b||/nu <= 1/2 (Psi-bound), K'_A = 2||U||A_0/nu: need a_{j,min} -> a_min > 0 (true: F finite,
  a_j -> a in l_1, supp a_j = F) and nu_j -> nu;
* blocks: |d^{(j)}(omega)| <= ||D omega||_2 (since ||D w_j|| = C_j), radius conditions use gap^{(j)} (hypotheses are stated at f_j), C_min^{(j)};
* rebalancing: transfer data chosen AT f; by Lemma lem:persistence they persist at f_j (k_* stays a peak with positive margin, L_j built
  with |w_j| >= gamma, Y_j/q_0^{(j)}, e_{y,j}, iota_j, D y_j converge); Lemma lem:TV at f_j needs only ||W - w_j||_inf <= (M_j - gamma)/4,
  ||D(W - w_j)|| <= C_j/2, which hold with the limit constants and a factor 2 of room;
* K_3 uses h <= 2/q_0^{(j)}, H_m <= 2/sigma^{(j)}_m, e_y >= 1/2: convergent.
So all constraints on (c_flat, t_1) are uniform for j >= j_0 (j_0 depends on eta_1, i.e. on eps_tr). Also verified: Lemma lem:TV is
robust under the inward moves of Lemma 5.1 (sign of W at k in L is preserved because ||W - w|| < gamma), so the "inward coordinates"
extension of Lemma U (Z3 5.1) is also correct.

## 1.7 Theorem E (windowed recovery through nearby first rows). CORRECT. (Re-derived line by line.)
* (A) at f_j: Lemma U applied to the + data for 0 < rho r <= c_flat t_i and to the - data for -c_flat t_i <= rho r < 0; both represent
  g_{j,t_i}; Gamma <= 1 + eta_0/2 <= 2, eps_tr = eta_0/2 give 1 + (rho^2 r^2/2)(1 + eta_0).
* (B'): p*(f_j + r rho g_{j,t}) <= p*(f + r rho g) + eps_j + rho|r| K t <= s(rho r) + eps_j + rho|r| K t (g in C(f)).
* |r| <= r_0: if I_r != {} then rho|r| > c_flat t_{n} = 2 c_flat tau_j, so eps_j <= theta_j tau_j^2 < theta_j rho^2 r^2/c_flat^2 <= (1-rho^2) r^2/24;
  sum_{I_r} t_i < 2 rho|r|/c_flat (dyadic); extra <= (1-rho^2)r^2/24 + 2 rho^2 K r^2/(c_flat n) <= (1-rho^2) r^2/12 with
  n >= 48 rho^2 K/(c_flat(1-rho^2)). Then 1 + r^2[(1+rho^2)/4 + (1-rho^2)/12] = 1 + r^2(2+rho^2)/6 <= 1 + r^2/2 - r^4/8 iff
  r^2 <= 4(1-rho^2)/3, true for r^2 <= r_0^2 <= 1-rho^2; and s(rho r) + (1-rho^2)r^2/12 <= s(r) by Lemma lem:slack(a).
* |r| >= r_0: extra <= eps_j + 2 rho K T_j|r|/n <= (1-rho^2) r_0|r|/3 <= (1-rho^2) min(r^2,|r|)/3. Checked.
* Averaged data: d-neutral two-piece data at f_j (all defining conditions are linear or convex, d^{(j)} linear); Gamma^{(j)}_w convex;
  rho^2(1 + eta_0/2) <= 1. Corollary cor:D1 at f_j (F finite, I finite) gives (f_j, rho gbar_j) in cl NA, and (f_j, rho gbar_j) -> (f, rho g).
Comment: (E-e) is natural: eps_j enters only through pieces finer than the probing scale, which exist exactly for |r| >~ T_j 2^{-n_j}.
Theorem E is a clean, correct and useful generalization of the mechanism of Theorem thm:S (f_j = f).
Observation (used in part 4 below): Theorem E allows ANY sub-window (T_j, n_j); it is not tied to the design windows. Hence in
Corollary 3.4 the bottom T_lo(l_j) of the design window may be replaced by 2^{-n_j}T_hi(l_j) for any n_j <= n^w_{l_j} with
n_j/((1 + C_H)K_*) -> infinity ("top sub-window"); the exactification threshold then becomes theta 4^{-n_j} T_hi(l_j)^2 with n_j ~ psi K_*,
instead of theta 4^{-n^w} T_hi^2. This is what the notes' own gloss "tower gaps: r_next <= exp(-C prod(1/r))" (4.3(i)) actually needs.
