# cert0 notes part 1: KN^tr Steps 0-4, KN-1, S-0, D1-D3, K1 (re-derivation, findings)

## Step 0-3 (ratio space)
- Step 0: (C1),(C2); active weak peaks of (T)-blocks pushed to rho = 1-b (value change <= 2b theta Phi/m).  r_1 := formula-1 ratios.
  F(r_1) <= max_{N_T} rho_d(f_1) <= 1 + C_* b by Lemma F (needs P(f_1) ⊇ P_rob, Omega ⊂ Q; with K1 also OK before the push up to O(b)).
- Step 1: Lojasiewicz on compact K_kappa (Q3): r' in Z, |r'-r_1| <= C_L g(r_1)^{2/N_L} <= eta'/3 by (D1).  Needs Z ∩ K_kappa != {}:
  else g >= g_min > 0 on K_kappa (design number), contradiction with g(r_1) <= (1+Lip C_*)b once Design dominates 1/g_min [V2 Lemma L alt (i)].
  F(r') <= F(r_1) + Lip*_kappa eta'/3 <= 1 + delta_0(b)  [P-LIP: Lip must include 1/Phi_d].
- Step 2: QC(b) + (D2): Y_1 nonempty (else F >= 1+m_0 > 1+delta_0), dist(r',Y_1) <= C_Y delta_0^{alpha_Y} <= eta'/3.
  [Convention mismatch X1 2.5(b) "dist <= C_Y (F-1)^alpha" vs X1-ref 7(b) "dist^{1/alpha} <= C_Y (F-1)": (D2) in Q1 (S6) matches X1's form.
  Cosmetic: either form, constants are design numbers.]
- Step 3: G_h(r_1') <= 1 - mu(h); inf over OPEN ball not nec. attained -> choose r'' with F(r'') <= 1 - (3/4)mu (cosmetic).
  |r''-r_1| < eta'.  Robust minors >= u - Lip* eta' >= u/2; signs of r_d kept.

## Step 4 joint fixed point -- set-up (my re-derivation)
Fixed (one-shot) moves first: TU pulls of all TU carriers, (KN)-lever pushes (size s_0, eta' version), D2 pushes (size eta').
Continuous unknowns: bank masses m_l (l in L_0 := active Omega carriers of all active blocks ∪ class-G nearly-neutral coarse strict non-peaks of
(T)-blocks), z-move amounts y_l on free coords of S^nat (class-R nearly-neutral carriers of (T)-blocks; robust two-sided room >= u by class R),
one kappa-push amount s_m per block.  Equations: val_l = r''_l kappa*_m (active; (U)-blocks s_m r''_l), val_l = 0 (holds), kappa_m = kappa*_m.
Jacobian: d val_l/d m_l = s'^2 v'/N (diag, >= Design^{-1/6}/2); d val_l/d m_k = O(C Design eta_*) (Hilbert normalization, Lemma B);
d val_l/d y_l = v_l(j) (diag), d val_l/d y_k = 0 (disjoint signature sets, z-moves do not change e);
d val_l/d s_m = second order; d kappa_m/d s_m in [3/4,1] (Lemma 1.4(a), X_m <= C c^2 D^2); d kappa_m/d val_l = rho_l M X/C = O(c^2 D^2).
=> near-diagonal, invertible, contraction (V1 explicit fixed point).  STATUSES in (T)-blocks depend only on (r_d, sigma, R^2) (Lemma K / K1):
r exact, R^2 = R_a(r'')^2 exactly (holds), sigma in [sigma_rob, sigma_rob + C c^2] => rho_d <= (1-3mu/4)(1 + C D^C c^2) <= 1 - mu/2.

## FINDING F1 (precision, fixable): the KN-1 hold pull window
V1 Lemma TU Step 2: m_l = (Delta_l N + beta_l (N - nu_p))/(s'^2 v'_l),  Delta_l = x_l + 2 v_l(j_l) + O(...),  N - nu_p <= C Design eta_max^2,
beta_l = eps_l <U^*u_l, e^p> of EITHER sign (|beta| <= ||U||).  Positivity of the bank needs Delta_l nu_p >= |beta_l| (N - nu_p) when beta_l < 0,
i.e. v_l(j_l) >~ |x_l| + C Design eta_max^2.  Q1 2.2's per-carrier rule "v_l(j_p) >= max(needed correction, c_{L+1})" with the first-order
correction (KN-1 holds of nearly neutral carriers can have |x_l| ~ 0) and the floor c_{L+1} <= b^2 << Design eta'^2 does NOT guarantee a
nonnegative bank when beta_l < 0.  FIX: take all pulls of the joint fixed point in the COMMON window [eta_*, 2^G eta_*],
eta_* := max(|x|_inf, c_{L+1}) (= V1 Lemma TU verbatim with eta := eta_* >= |x|_inf; its proof uses only |x|_inf <= eta), or per carrier
v_l(j_l) >= max(|x_l| + C_T eta_*^2, c_{L+1}).  Then m_l >= c_f eta_* >= c_f c_{L+1}, pull mass 24 lambda v >= 24 c_{L+1}/Design (BR (U3)),
cost C_T eta_* log(e/eta_*) <= C_f Design eta' log(1/eta') + C c log(1/c); pulls still << v_l(second element) (refb 1.4 (D-lev) unaffected).
Numerical illustration: cert0_work/tu_bank_check.py (TODO).

## Other checks (OK)
- K1 identity: re-derived algebraically (kappa = A + theta[Phi_{P\Omega}^2 + sum_{Omega∩P}(1-rho^2)Phi^2] + S_f/theta; a^2 = sigma' + k^2R^2). Numerics TODO.
- D1: (U)-block r^(m) only in (X3)_m (Delta'_m removed): minors homogeneous deg 0/1; cofactor columns homogeneous deg e_J in {0,1} -> minors of
  g_J homogeneous.  Robust values scale by >= s^n: after rescaling robust minors >= u/4 (not u/2) -- cosmetic (Hoffman bound unchanged up to 2).
- D2: (U)-block inactive near-threshold pushed inward by eta'; second-order effects O(Design^2 eta'^2) << eta' margin.
- D3: |rho(f) - rho^0(r(f))| <= C D^C (b + c^2) in formula-1 convention: |sigma'-sigma_rob| <= 3b + c^2, |R^2 - R_a^2| <= C b^2 (rho<=b carriers),
  dK/dsigma, dK/dx <= C D^C on {sigma >= D^-2, 1-R^2 >= sigma_rob/4}.
- KN-1 hold realization: class G (after (C1): exactly swallowed on S^nat ⊇ far part) -> TU; class R (both signed rooms >= u ||v 1_{S^nat}||)
  -> z-moves on free coords of S^nat (exact, local: z-moves do not change e).  Both available.  OK.
- S-0 in route V: Step B changes zeta only by fine carriers (sum lambda <= C c_{L+1}) and released far parts (<= 4c^2 per coarse value);
  clamp equation (slope from robust peak) => |Delta C_m| <= C_f c_{L+1}; rho_k = v_k C/(Phi_k M) => relative status drift C_f c_{L+1}
  (even better than C Design c).  kappa (= (A^2 - C S_Omega)/(A M)) Lipschitz => |kappa^# - kappa'| <= C_f c_{L+1}.  OK.
