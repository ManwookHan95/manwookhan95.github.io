# Y1 part 5c — Corrections/generalizations to parts 5a, 5b (self-check)

## 5c.1 Window-level repair directions (generalizes (DR); replaces "compensated" in (Cmp_w), (NN_w))
**Definition (Rep^s_m at w).**  For a block m and s in {+-1}: there is rho in R^G_{>= 0} (G = class-G coarse carriers at w), ||rho||_1 <= 1,
with zero cost AT f^#_w (V(rho) z^#-signed, supported in K^#), supported on carriers that are strict non-peaks of f^#_w, with
gap^# >= M_m u(w)/4 at every member l'' with q^#_{l''} < 0, and with d-sums at f^#: sum_{m(l'')=m} q^#_{l''} rho_{l''} = s d,
d >= u(w)/Design(l), and sum_{m(l'')=m'} q^# rho = 0 for m' != m.
Block m is COMPENSATED AT w if (Rep^+_m) and (Rep^-_m) hold at w.
**Lemma 5.1' (fixed repair directions).  PROVED.**  If (DR^s_m) holds at f (Z4), then (Rep^s_m) holds at every clean w of level l >= l_f.
Proof.  Lemma 5.1 (u-values of repair carriers unchanged, d-sums s A_m/A^#_m and 0, zero cost at f^#), normalization by ||rho||_1 <= R_f:
d = A_m/(A^#_m R_f) >= u(w)/Design(l) for l large; repair carriers are fixed strict non-peaks of f with fixed gaps, which persist at f^#
(Lemma 4.2(c): fixed relative positions are robust for l large).  QED
Other sources of (Rep^s_m) at w: any single resonant G-carrier which is a strict non-peak of f^# with |q^#| >= u(w)/Design(l) of sign s
(and robust gap if s = -) — e.g. a near-threshold resonant swallowing-type peak converted by the threshold raise (q^# ~ Phi M/(mC)).
Revised hypotheses: (Cmp_w) every block is compensated at w or sigma-one-signed at w; (NN_w) in a sigma-one-signed block no kept
carrier has sigma q^# > 0, and if some kept carrier has sigma q^# < 0 then (Rep^sigma_m) holds at w.
Proposition 5.2, Step 3 (revised).  For a compensated block m: c := |Q^#_m(tau_0)|/d, tau' := tau_0 + c rho^{m,-sgn Q^#_m(tau_0)}; for a
sigma-one-signed block with Q^#_m(tau_0) != 0: sgn Q = -sigma by (NN_w) and tau' := tau_0 + (|Q|/d) rho^{m,sigma}.  The d-sums are
block-diagonal at f^# by definition, so all d-rows become exact; ||tau' - tau_0||_1 <= N K_Q t Design(l)/u(w); the repair amounts give
|omega| <= c rho_{l''}/lambda_{l''} <= K_Q t Design(l) D(l)/u(w) <= 1/t at the repair carriers for t in W(w), l large (K_Q t^2 Design D/u
<= C_f T_hi(w)^2 Design^2 u^{-4} -> 0), so A_2 := 22 works; members with q^# < 0 are of kind [2] (gap >= M u/4), members with q^# > 0 of
kind [3] after the shift (or kind [2]).  K_U is now K_g + 1 + G** V_w/t + N K_Q Design(l)/u(w).  Everything else in 5a is unchanged.

## 5c.2 Window arithmetic (constants of parts 3 and 5)
With D := D(l), u := u(w): K_g <= C D/u, K_d, K_P <= C_f D^3/u, K_O <= C_f D^5/u^2, V_w/t <= C_f l D^5/u^2, K_Q <= C_f G** l D^5/u^2,
K_U <= C_f G** l D^5 Design(l)/u^3 (the factor Design/u comes from the normalization d >= u/Design of (Rep)), and
K_w <= C_f (1 + G**)(K_U + K_P + 1) <= C_f Design(l)^3 u(w)^{-3}, because Design(l) = X^6 with X >= l D(l) G**(l).
This is why Definition 1 uses Q(w) := Design(l)^4 u(w)^{-omega(l)-8} (a first draft used Design(l) u^{-omega-4}, which does not
dominate Design^3): K_w/c_flat(w) <= C_f Design^3 u^{-4} = C_f Q(w) u^{omega+4}/Design <= C_f Q(w) u(w), hence n(w) c_flat/K_w >=
l 2^{l^3}/(C_f u(w)) -> infinity, and K_w T_hi(w) <= C_f Design^3 u^{-3} 2^{-l^3}/(l Q(w)) <= C_f 2^{-l^3}/l -> 0.  Theorem 1 only uses
Q >= Design and Q >= u^{-4}, so it is unaffected.  (E-e'): T_lo(w) <= 2^{-n(w)} <= 2^{-u(w)^{-4}}.

## 5c.3 Other checks done (all consistent)
* Pigeonhole is per level: each sub-window band is an open interval, each rate lies in at most one band.
* Fine carriers: sum_{l'>l} lambda <= b(w)^2/2 for every sub-window of level l (c_{l+1} <= b(l, M(l))^2), so fine perturbations of
  every coarse quantity are O(b^2), below every tiny threshold.
* Donor feasibility uses Design >= 2^{6 sigma(l)}; with the corrected Q(w) still T_lo(w)^3 <= 2^{-18 sigma(l)}.
* Statuses at f^#: every KEPT coordinate is a strict non-peak of f^# (robust ones by Lemma 4.2(c); (K4) only in raised blocks, where
  they become strict non-peaks; (K3) has rho^# <= C b); DROPPED coordinates may change status, which is harmless (5a Step 5).
* (SP_w), (Cmp_w), (NN_w) are statements about f at level l and the explicit companion f^#_w; they involve no rate thresholds beyond
  u(w), b(w), which are design numbers.
