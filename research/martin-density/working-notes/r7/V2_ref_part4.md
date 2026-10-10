# V2-ref part 4 — Part 4 of V2 (shifted data) and Master Theorem III

Sources re-read: def:twopiece, def:SLD/thm:SLD ((P1), (T-d)), lem:threshold, Lemma A(d) (smoothness of |.|_m), Z3 Lemma 3.1,
Z4 Lemma 5.0, Z4-ref Prop. 5.6', Y1 Corollary M1, V1 Master Theorem II and the V1 referee report (V1 correct in all PROVED claims).

## 1. Proposition C3 (rigidity of shifted data).  VERDICT: CORRECT (PROVED).
Subtracting the two representations: b^+ - b^- = sum_m R_m^*(omega^-_m - omega^+_m) - W_Delta, R_m^* e_k = lambda_k u_k; at j outside
Sigma_Omega (which contains F) the first sum vanishes; two-piece data give (b^+ - b^-)(j) = 0 off F ∪ K and z_j(b^+ - b^-)(j) >= 0 on K. ✓
Sharpening (free): only SWITCHING carriers (omega^-(k) != omega^+(k)) need to be excluded; carriers with equal data on both sides
(e.g. clamped fine coordinates of window data) do not enter.  Note Sigma_Omega = F ∪ union_{k in Omega}(supp y_k ∪ S_k) for the
SLD designs ((P1)), a finite union of signature sets plus a finite set — never cofinite.

## 2. Corollary C3.1.  VERDICT: (a) CORRECT; (b) CORRECT (design fact) with the HEURISTIC reading properly labelled; (c) CORRECT
ONLY FOR CONSTANT-SIGN MAXIMAL CONTACT — precision (P4.1).
(a) For j in S_l far out (l notin Omega): W_Delta(j) = Delta_{m(l)} lambda_l w_m(k(l)) v_l(j) + (finer targets, <= ||Delta||_1
2^{-2j} c_l delta_l by allowedness (b)), coarser targets avoid S_l (allowedness (a)), other signatures vanish (disjointness): the own
term dominates for j beyond a point depending on Delta, so Prop. C3 forces |z_j| = 1 with z_j = -sgn(Delta_m w_m(k(l))). ✓
(b) y_l = y^{(i_{k(l)})}: the target of carrier (k, m) is indexed by k with the SAME sequence (i_r) in every block, every i occurs
infinitely often and is allowed at all large levels (thm:SLD (T-d)), and y^{(i)} close to e_j^*/q^*(e_j^*) has y^{(i)}(j) >
1/(2 q^*(e_j^*)) (q^* >= ||.||_1). ✓
(c) (P4.1): "at maximal contact (z = +-1 off F) ... (SP_w) holds" is proved (Y1 Cor. M1 via Z4 Lemma 5.0) only for z = eps_0
CONSTANT off F: then every carrier is swallowed with eps_0 and the robust peaks of Z4 Lemma 5.0 with w = +-M are of swallowing type
(L2) and anti type (U2).  For FULL but SIGN-MIXED contact (|z| = 1 off F, signs varying) the identities of (b) are void (no free
coordinates) but (SP_w) can fail: the self-aligned configuration z = sgn w_m(k) on S_k for every coarse peak k makes every coarse peak a
class-G peak of swallowing type, so a block can lack an upper source as soon as it has an anti-type strict non-peak with robust
relative position; case (II) is then not excluded by the cited results.  Fix: read "maximal contact" as z = eps_0 off F.

## 3. Proposition C4 and the Example.  VERDICT: CORRECT (PROVED).
At s in S^nat_l \ Sigma_Omega: h(s) = b^+(s) - d_m(omega^+_m) lambda_l vs M'_m v_l(s) - (finer targets), eps b^+(s) >= 0 (z' = eps_l);
summing over S_i and dividing by V_i gives the sandwich; |A_1 - A_2| <= |Delta_m| lambda M' + tgt(1/V_1 + 1/V_2) in both signs of Delta;
|A_i(g) - A_i(g_t)| <= ||g - g_t||_1/V_i. ✓  Scope (correctly stated by V2): rows at which l is still a PEAK.  At a companion that
turned l into a strict non-peak, switching at l itself enlarges the sandwich (by eps lambda (omega^- - omega^+)(k(l))) and d-neutral
data could follow the oscillation; for a ROBUST peak this needs a move of size ~ margin, i.e. not a cheap companion — so the
reading "d-neutral data cannot follow persistent oscillations at cheap companions" is right.  Also consistent with Theorem C1: an
oscillation D > 0 forces |Delta d^{dec}| >= D/(lambda M) - O(t) at every scale, hence case (II) at every clean sub-window.
Example: re-verified: kappa = c C/(Phi^2 w(k_1)) gives d(omega^+) = c and sgn(-kappa) = eps_{k_1} (anti type), so -kappa lambda u_{k_1}
is z-signed; side - needs phi <= c z (R_m^* w_m) pointwise on S^nat_l (the note's "phi <= c lambda M v_l" ignores the finer-target
part of R^* w; with exact coherence z R^* w >= 0, so choose phi below c z R^* w); g(xi) = 0 by the choice of b_0 (a(zhat) = 1).
It is conditional on EXACT coherence (R_m^* w_m vanishing at every free coordinate — infinitely many identities by C3.1(b)); no f
with partial contact satisfying it is exhibited.  Labelled correctly as a data computation.

## 4. Lemma C5 (fine-tail completion).  VERDICT: CORRECT (PROVED).
K = [-1,1]^{J_fine} (J_fine countable) is compact, convex, metrizable in the product topology; z' -> R_m^** zhat(z') is continuous into
l_1 (each lambda_k u_k(.) by dominated convergence, sum_k lambda_k ||u_k||_1 < infinity); R_m^** zhat(z') != 0 (a(zhat(z')) = 1, and
R_m^** is injective on l_infty because {u_{k,m}}_k is dense in S_Y and Y is dense in l_1); J_m is norm-to-weak* continuous (Lemma A(d));
W(z')(j) continuous by dominated convergence; the clamp map has a fixed point (Schauder-Tychonoff), and the fixed-point equation gives
exactly the three cases.  Coarse vectors vanish on J_fine (supp u_k ⊂ supp y_k ∪ S_k ⊂ T(l) ∪ S_k for k <= l), so coarse values are
EXACTLY unchanged; Z3 Lemma 3.1 with sum_{k>l} lambda_k <= T_lo(l)^3 gives the cost. ✓
Limitation (precision P4.2, relevant for C6): the completion is for ONE shift vector Delta.  W is linear in Delta, so it also
completes every positive multiple of Delta, but not a two-dimensional family: a common fixed point making W_{Delta^(1)} and
W_{Delta^(2)} simultaneously admissible needs each X_m := R_m^* w_m to vanish at free coordinates and to be z-signed at contacts
(if the Delta^(r) span the shifted blocks), which the clamp construction does not give.

## 5. "Near-coordinate conversion" (SKETCH) and Theorem C6 (SKETCH).  VERDICT: plausible SKETCHES; gaps as listed by V2 plus
two more.
V2's gaps: (g1) exactification of the block scalars (theta_m, A_m) entering the shifted system (Remark 4.5 shows the Jacobian of
(theta, A) w.r.t. one peak push and one strict non-peak push is rho_k M/Phi_P^2 > 0 — CORRECT, re-derived and checked numerically,
part 1 §5 — but a robust strict non-peak with w != 0 that is not itself a variable is not guaranteed); (g2) the near-coordinate
conversion; (g3) (SC) at the companions in configuration (i).
Additional gaps found here:
 (g4) [several shifted blocks] In case (II) the actual shift delta(t) is NOT pinned, so its DIRECTION may vary with the scale t inside a
      window; Theorem E averages data of all scales of the window at ONE companion; Lemma C5 completes only one ray of shifts
      (P4.2).  With one shifted block (or shifts confined to a fixed ray) this is harmless; with two or more independently shifted
      blocks the sketch needs either per-block admissibility of each R_m^* w_m on the fine tail or a transplant that forces all
      scales of a window onto one shift ray with error O(K t) — neither is provided.
 (g5) [joint fixed point] Lemma C5 changes z on J_fine, hence the fine residues on the COARSE coordinates that (ST_w) is supposed to
      absorb; completion and absorption must be done jointly (e.g. Schauder-Tychonoff on (z'_fine, coarse data), using that under
      a Slater condition the coarse absorption depends continuously on the residue).  Plausible, not written.
Possible route for (g3) (SKETCH, mine): (SC) at a companion f_j fails only through peaks with margins, and strict non-peaks with gaps,
below Upsilon s for s in a sequence -> 0.  Choosing s_{l'} with Phi_{l'+1} << s_{l'} << (signature room of level l') — possible since
Phi_{l'+1} <= c_{l'+1} <= T_lo(l')^3 is far below delta_{l'} 2^{-2 min S_{l'}} — the carriers of levels > l' contribute <= 2 Phi_{l'+1}
= o(s_{l'}), and the carriers of levels <= l' contribute only if near-degenerate; a regularizing companion that pushes, level by
level, every fine carrier by its own far signature coordinates to margin/gap >= (its signature room)/2 (cost <= sum lambda_k x room,
negligible; threshold drift of finer pushes <= c_{l'+1}) makes all these contributions vanish.  This interacts with Lemma C5 (same
coordinates), see (g5).

## 6. Master Theorem III and the residual list.  VERDICT: CORRECT (PROVED), given V1 (now refereed: correct in all PROVED claims,
r7/V1_referee.md) and the precisions (P2.2), (P3.1).
V1 Master Theorem II uses (SH_w) only through |Delta d_m| M_m <= K_d' t (V1 Step 0; V1-ref) — supplied by Theorem C1(I) with
K_sh <= C_f Design^3/u^3 (the u-powers of K_P, K_O, K_w grow by at most two, absorbed by Q(w) = (4 Design/u)^{omega+20}) — and
(VR_w) only in Step 3 (ray removal) — replaced by the Hoffman projection of Theorem B (part 2 §4: V1's later steps use only
|tau - tau'|, the rows tau' >= 0 / = 0 and the box).  V1's other estimates use only upper bounds on b(w) and on the tuning size
(eta Design <= T_lo^4/l still holds, part 2 §3).  Residual (logical contrapositive): f notin Rec only if at all but finitely many
levels EVERY clean sub-window has rho^sh(kappa(w), f) <= b(w) (then I_sh(w) != {} automatically).
Sharpening (P7, see V2_ref_part3 §3 and V2_ref_notes 4b): since V1's Lemma S pins the shift under (SH_w) independently of rho^sh, and
Theorem B removes (VR_w) in either case, Master Theorem III' holds: f in Rec if infinitely many levels have a clean w with
rho^sh >= u OR (SH_w).  Residual: rho^sh <= b AND c_pi <= b at every clean w of all large levels.
