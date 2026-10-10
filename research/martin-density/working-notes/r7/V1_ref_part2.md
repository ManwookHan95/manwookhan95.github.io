# V1-ref part 2 — verification log: design, Lemma D, Lemma S, Lemma B/DR, Lemma TU, Lemma IP

## Theorem 1' (D_Omega)
(a),(b),(c) re-derived: S_l = {2^l(2i+1)} pairwise disjoint (2-adic valuation l), avoid j0 = 1, gaps exactly G_l = 2^{l+1};
allowedness (a)-(c) satisfied by every finitely supported target at large l (c_l -> 0, l >= max supp); sum_{l'>l} c_{l'} <= (4/3)c_{l+1},
lambda_{l'} <= c_{l'}/4, so sum_{l'>l} lambda <= b(l,M(l))^2/3; bands: b(w) <= 2^{-4n(w)} <= 2^{-64/u(w)} < u(w), u(w^+) = b(w).
Design(l) contains 2^{G(l)} = 2^{2^{l+1}} explicitly (doubly exponential; harmless, it is a design number fixed at stage l).
(d) survival: a meta-claim; the only changes w.r.t. D_X / D^PW / D^Y are larger Design and Q (more rate objects, exponent omega+20) —
every listed window proof uses Q, Design only through upper bounds "T_hi x factor -> 0", "n / factor -> infinity". Accepted.
PRECISION (p1): l_f must also satisfy s_max(l_f) >= max F (needed for s_m notin F, pulls/banks notin F, and
"z^2 = eps on S_{l''} \ [1, s_max(l)]" in Lemma TU). s_max(l) -> infinity because every target y^(i) is eventually used and
the targets are dense in S_{q*} ∩ c_00 (a dense subset of c_00 cannot have uniformly bounded supports). Y1 part 3 already
puts "l_f >= max F" — for V1's far moves the needed condition is s_max(l) >= max F (Y1-ref m3 uses the same fact).

## Lemma D — CORRECT
Checked against lem:threshold (||alpha||_1 = 1, supp alpha ⊂ P), eq:margin (sigma|alpha(k)| = lambda mu, margin
mu = |xi(u_k)| - vartheta Phi = q_0 Phi theta (rho-1)/m), lambda_k = m Phi_k, sum_k Phi_m(k)^2 <= 1/12, mu <= |xi(u_k)| <= 2q_0.
Coarse tiny-margin peaks carry <= (M_m/(4C_m)) b, fine peaks <= q_0 b^2/sigma_m; M_m/C_m, q_0/sigma_m are f-constants (N finite;
C_m > 0 by lem:threshold). Clean w excludes rho in (1+b, 1+u).

## Lemma 3.4' — CORRECT (re-read Y1 Lemma 3.4: the upper-bound proof uses (U1)-(U3) only, the lower-bound proof (L1)-(L3) only).

## Lemma S — CORRECT
eq:peakshift: |omega_+(k)| + |omega_-(k)| = -vs_k Delta Theta_m(k) - Delta d_m M_m >= 0, and <= t/(sigma|alpha(k)|) if alpha(k) != 0;
hence -Delta theta = vs lambda (Delta d M + e_k), lambda e_k <= t/mu_k. lem:switchbudget: sum_{j notin F} phi_{z_j}(Delta B(j)) <= t/q_0.
lem:phicalc(c): 2-Lipschitz. (a): uses Lemma D only. (b): the decomposition of Delta B 1_{F^c} and the inequality
c_pi ||delta||_1 <= c(delta; pi) <= t/q_0 + 2||R||_1 re-derived; c(.;pi) positively homogeneous (x scales), finite (phi_z(x) <= 2|x|).
Blocks outside I_up ∪ I_lo: both sources -> Lemma 3.4'. Class-R peaks in I_lo blocks with rho in [1,1+b]: in the class-R error (3.1).

## Lemma B (formula (3.1)) — CORRECT (direct computation; X ⊥ U^*A^0 needs J ∩ supp A^0 = {}).
## Lemma DR — CORRECT (constants: s_{s_m}^2 v_{c}(s_m) >= 8^{-sigma(l)} delta_min/2 since n_c <= 2; lambda_c = m Phi_c >= 1/D(l);
nu <= ||U|| = 1/2; so mu^D <= 2 D 8^sigma Lam/delta_min <= Design Lam). Case (a): eta_m <= 1 - vs z^1 keeps |z^2| <= 1.

## Lemma TU — CORRECT (explicit fixed point re-derived; numerics)
m(y) solves the l''-th equation iff N(m) = y (checked); Phi'(y) = sum m(Delta+beta)/(v' Phi) — the contraction constant involves
1/(s'^2 v'^2) (not 1/(s'^2 v')): both are design numbers of level L, absorbed in c_T = f-const x Design^{-3}.
V1_ref_work/tu_check3.py / tu_check4.py (diagonal base, 1-4 tuned carriers, long bounded-gap signature sets, pulls with
v(j) in [eta, 2^G eta], mu = 24 lambda v(j), banks at the first far signature coordinate, scalar fixed point by iteration):
1227 tests inside the smallness regime: |val^# - val^(2) - x| <= 1.8e-15 (EXACT), all bank masses > 0, |Phi'| <= 0.018 at the
fixed point, all increments Delta >= eta/2, other carriers moved by <= 0.44 x (Lemma B(i) bound C||X||^2), i.e. O(eta^2) with a
model (design) constant (per-model ratio other/eta^2 constant across eta). Outside the regime (eta not << s'^2 v'^2 nu, or signature
set too short to host a pull with v(j) ~ eta) the iteration can diverge: consistent with the hypothesis eta <= c_T.

## Lemma IP — CORRECT
A'(theta) >= A - theta b sum_N Phi^2 - E; B'(theta) <= B - theta(c - 2theta b) sum_N Phi^2 + 2 theta E (identity
theta^2(1-b)^2 - (theta(1+b) - c_k)^2 = (c_k - 2theta b)(2theta - c_k); theta(1+b) - c_k >= theta/2 > 0); B = A^2 (Lemma T(b));
Psi'(theta) >= theta c sum_N Phi^2/4 > 0 => theta' > theta by Lemma T(c). V1's lemma_ip_check2.py re-run: 3942 tests, the 13 flagged cases have
predicted relative raise 1e-20..3e-17 (below double precision). Not used in the assembly.
