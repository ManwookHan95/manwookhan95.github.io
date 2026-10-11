# G3 referee notes (Round 14): proofs of the verdicts, fixes and referee additions

Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  "Mod chain" = modulo the refereed links cited by G3 (Part III Sections 2-5,
Part II Sections 4-5, K1/K2, J1/J2, H1/H2 and their referee reports) and G1/G1-ref, G2/G2-ref of this round.  Part files:
r14/G3_ref_part1.md (Section 2 of G3), G3_ref_part2.md (Section 3, numerics N2, N3), G3_ref_part3.md (Sections 4-6).
Scripts and outputs: r14/G3_ref_work/ (refmodel.py; check_universal.py; test_pin.py, test_pin2.py, check_resc.py;
test_fr.py, test_fr_ctrl.py; *.out).  Notation as in G3 Section 1: f = a + L^*w, q*(a) = ||a||_1 + nu = 1, zhat = z + h,
h_s = (mu*_s)^2 a_s/nu (diagonal base), xi = q_0 zhat, sigma_m = |zeta_m|_m, q_0 + sum sigma_m = 1, V = B_+ - B_- =
sum_k gamma_k u_k, e_j^+- the coordinate excesses, sum_j (e_j^+ + e_j^-) <= 2(s(t) - 1)/q_0 <= t^2/q_0.

## A. Re-derivation of the universal lemmas (G3 Section 2)

A.1 All of Lemma 1.1, Lemma 1.2, Cor. 1.3, Lemma 1.4 (a)-(c) and (1.1), Theorem CL (CL0)-(CL2), Cor. CL.1, Lemma 1.5,
Cor. 1.6, Lemma 1.7 (i)-(ii), Cor. CL.2 and Cor. 1.8 were re-derived line by line (details in part 1); every step is
correct.  Two points worth recording:
 (a) The identity ||alpha||_1 = 1 in the block threshold structure zeta/sigma = alpha + D^2 w/C: with N(w) = M + C = 1 and
     zeta/sigma = alpha + D beta, ||alpha||_1 <= 1, ||beta||_2 <= 1, one has 1 = <w, zeta/sigma> <= M ||alpha||_1 + C, which
     forces ||alpha||_1 = 1, alpha on the peaks with the signs of w, beta = Dw/C.
 (b) Remark (1) after Lemma 1.7: Lemma 1.1 gives sigma G(W_+) <= s(t) - 1 and G(w + t Theta) >= t |alpha(k)| (max_P sgn(w) Theta -
     sgn(w(k)) Theta(k)), so peaks in supp alpha are within t/(2 sigma |alpha(k)|) of the common maximum; weak peaks (small
     alpha(k)) and degenerate peaks (alpha(k) = 0) are not controlled, and they enter S_1 through M Phi_k^2 Delta Theta(k)/C.
     (P1) is a genuine hypothesis.
A.2 Numerics N1 (independent two-block implementation, 40 random instances x 4 random feasible decompositions, t in {.3,.1,.03}):
every inequality of Lemma 1.4, Cor. 1.3, Theorem CL (random thick sets T), Lemma 1.7 Step 1 and (i)-(ii) and Theorem 2.10
(random G, random J_c of arbitrary coordinates) holds; worst normalized slacks <= 2e-17 (ties) and negative otherwise.

A.3 PRECISION P-CL1 (reading of Theorem CL; interpretive).  With T = F one gets the cleanest form
      ||V 1_{F^c}||_1 <= - sum_{s in F} zhat_s V_s + 3t/q_0      (h = 0 off F),
and by Lemma 1.4(b) a support coordinate s absorbs at most 2|a_s|/t + O(t) of anti-signed switching.  So "thick" in
Theorem CL is SCALE-RELATIVE: at scale t a support coordinate with |a_s| >~ t |u(s)| is two-sided for practical purposes.
alpha(N cap F) in (CL2) is the total non-thick support mass of the ROW; at window scales of an (R1) stage
(s_1 <= theta_0 T/(8 rho A_0) << theta_0 = b/Des^{C_P}, (L-K2-1)) the term 4 alpha(N cap F)/t is large and Cor. CL.1 is
uninformative there; CL.1 states this alternative correctly ("or thin support at scales t <~ alpha/P_k").
A.4 PRECISION P-16 (Reading after Cor. 1.6).  "the anti-data-sign direction is pinned with the design constant 1/U_N" holds
only when alpha(N_l) <~ t^2 (near coordinates contacts, or t >~ alpha(N_l)^{1/2}); at f the near coordinates of (R1)
kind-(iv) carriers are contacts or b-thin data-sign support, so at window scales t << b the anti-data direction is in
general NOT pinned (numerics N2 (i), anti-data column).  The data-sign statement (pinned by U_far up to alpha(E_far)/t)
is correct.  Cor. 1.8 is correct under its hypothesis alpha <= t^2.

## B. Unshifted blocks (G3 Section 3)

B.1 Theorem 2.10 and Cor. 2.11 are correct (part 2).  Cor. 2.11's constant contains E(t), i.e. r_Q (other strict non-peaks),
Psi_J, Psi_k (carriers outside G) and eta_P ((P1)); "depends only on P_k, q_0, sigma" is true relative to these
(precision P-211).

B.2 REFEREE LEMMA R-ESC (escape lemma; sharpened form of Cor. 2.11).  PROVED (any admissible T, any row, mate, scale).
Fix a block satisfying (P1) at scale t (S_1(t) := t/q_0 + (sigma/q_0) eta_P (1 + M Phi_P^2/C)), decompositions as in
Cor. 1.3, a set G of strict non-peaks, and a set J_c of coordinates such that every s in supp u_k \ J_c (k in G) is PRIVATE
to k within G: V_s = gamma_k u_k(s) + psi_s with psi from carriers outside G.  The private coordinates may be contacts,
free coordinates or support coordinates of ANY mass.  For k in G with gamma_k != 0 put eps_k := sgn gamma_k and split its
private coordinates into A_k := {eps_k z_s u_k(s) > 0} (aligned), R_k := {eps_k z_s u_k(s) < 0} (anti-aligned), and put
  N_k := sum_{A_k} |z_s||u_k(s)|,  F_k := sum_{R_k} |z_s||u_k(s)|,  Fr_k := sum_{private free s} (1 - |z_s|)|u_k(s)|,
  h_k := sum_{s in supp u_k} |u_k(s) h_s|,  Psi_k := sum_{private s} |psi_s|,  alpha(R_k) := sum_{R_k cap F} |a_s|.
Then
  (1) |gamma_k| F_k  <=  2 alpha(R_k)/t + t/(2 q_0) + Psi_k;
  (2) |gamma_k| Fr_k <=  t/q_0 + Psi_k;
  (3) sum_{k in G} |gamma_k| (N_k - F_k - h_k)  <=  E(t) := S_1(t) + r_Q + t/(2 q_0) + 2 alpha(J_c)/t + Psi_J,
with r_Q := |sum_{Q \ G} u_k(zhat) gamma_k| and Psi_J := sum_{J_c} |psi_j|.  In particular the cushions of ALIGNED private
coordinates never enter, and the cushions of anti-aligned private coordinates enter only through (1).
Proof.  (1) At s in R_k, z_s V_s = gamma_k z_s u_k(s) + z_s psi_s = -|gamma_k||z_s||u_k(s)| + z_s psi_s.  Lemma 1.4(a) (s notin F)
and (b) (s in F) give z_s V_s >= -err_s with err_s = (e_s^+ + e_s^-)/(2t), resp. (2|a_s| + (e_s^+ + e_s^-)/2)/t.  Summing over
R_k and using sum (e^+ + e^-) <= t^2/q_0: |gamma_k| F_k <= sum_{R_k} err_s + sum |psi_s| <= 2 alpha(R_k)/t + t/(2q_0) + Psi_k.
(2) Lemma 1.4(c): (1 - |z_s|)|V_s| <= (e_s^+ + e_s^-)/t at free s; (1 - |z_s|)|gamma_k||u_k(s)| <= (1 - |z_s|)|V_s| + |psi_s|; sum.
(3) Theorem 2.10 gives sum_G gamma_k Rt_k <= E(t) with Rt_k = u_k(zhat) - sum_{J_c} u_k(j) z_j.  Since zhat = z + h and every
s notin J_c in supp u_k is private, Rt_k = sum_{private s} u_k(s) z_s + sum_{s in supp u_k} u_k(s) h_s, and
sum_{private} eps_k u_k(s) z_s = N_k - F_k (a coordinate with z_s = 0 contributes 0).  Hence gamma_k Rt_k = |gamma_k| eps_k Rt_k >=
|gamma_k| (N_k - F_k - h_k).  QED
Corollary R-ESC.1 (PROVED).  If every k in G has N_k - F_k - h_k >= c_k > 0 ("aligned-dominant in its switching direction"),
then sum_G c_k |gamma_k| <= E(t): the group is pinned at O(t) at EVERY scale unless E(t) is large, i.e. unless the shared
coordinates J_c carry support of mass alpha(J_c) >~ t sum c_k |gamma_k|, or carriers outside G switch at J_c (Psi_J), or other
strict non-peaks of the block switch (r_Q), or (P1) fails (shifted block).  Shared contacts and shared FREE coordinates are
never escapes; neither are aligned private coordinates, whatever their support mass.  The minors of the (X3)/FR/contact rows
do not enter: an EXACT resonance without an escape is pinned.
Corollary R-ESC.2 (kind-(iv) groups; PROVED as a norm-level statement, its use in the method SKETCH).  For kind-(iv) carriers
switching in their data direction, the near coordinates are aligned (definition of the data sign) and the far (pull-range)
coordinates anti-aligned; if the far mass is small (deep-swallowed, F_k <= U_far(k) << N_k), then c_k >= N_k - U_far(k) - h_k
>= c/H(L) (near mass >= 6/H(L), mod chain).  So an ACTIVE group (|gamma_k| >= K_* t) of such carriers in an unshifted block
needs E(t) >= c K_* t/H(L): a shared SUPPORT coordinate with alpha(J_c) >= c K_* t^2/(2 H(L)), outside switching at a shared
coordinate, or switching of other strict non-peaks of the block.  Method-level use (SKETCH): in the class bookkeeping
(K1 Lemma K1.2) r_Q contains the inactive strict non-peaks (<= K_lo t each), so the conclusion needs a threshold gap
K_hi >> K_lo n_Q H(L)/c between active and inactive levels (pigeonhole over a geometric threshold ladder); not checked
against K1's class count.
B.3 Numerics N2/N3 (part 2) confirm every prediction: aligned private thin support does not relieve data-direction switching
(test_pin (i): slope 6.3 down to t = .003 << cushion scale); a shared thin support target does ((iii): gamma'_+ = .41 at
t = .01, .90 at t = .003); a free shared target with an EXACT FR resonance and contact-only private coordinates is pinned
((vi): slope 2.25 at every t; test_fr control: slope 1.13 for M = 0, 1e-3, 1e-2); with a shared THICK target the FR minor
governs activity in the two-regime way of Cor. CL.2 (M = 0: 1.38 at every t; M = 1e-2: 1.32, 1.11, 0.74).  Lemma R-ESC
(1)-(3) verified term by term on 108 decompositions (check_resc.out; (1) nearly tight).

B.4 PRECISION P-29 (Cor. 2.9).  The bound C_v [(3t/(4q_0) + Psi_l)/(N_l/2 - |h_l|) + S_0/v_0] contains v_0 = min(val_+, |val_-|) and
C_v = max(1, val_+/|val_-|, |val_-|/val_+), f-data that are not design-controlled for nearly-zero-valued carriers, and the
hypothesis tau <= v_0 N_l/2 shrinks with v_0.  "DESIGN-controlled pinning constant" is wrong for 2.9 as written; the
design-controlled statement (Interpretation (a)) holds via Cor. 2.11 / R-ESC, whose constants contain no v_0.
B.5 GAP G-THIN (Interpretation (b) of Section 3, Section 6 "norm-level reading", RC_L).  Interpretation (b) lists "thin
support below its cushion scale" as an escape and then concludes "Persistent (R1) in unshifted blocks therefore needs ...
fresh kind-(iv) rows switching through shared THICK target support".  The conclusion drops the listed alternative.  By
R-ESC.2 the relevant cushion is that of SHARED support: a shared support coordinate of mass |a_s| removes the obstruction
(3) to relative activity K_* t exactly at the scales t <~ (2|a_s| H(L)/(c K_*))^{1/2}, and numerics N2 (iii) show that the
relief is real (gamma'_+ = .41 at t = .01 and .90 at t = .003 through a shared target of mass 1e-3, while the same pair is
pinned at t = .1).  Window bottoms satisfy s_1 << theta_0 <= b, so ANY shared support of mass >~ K_* s_1^2 H(L)/c (for
instance b-thin or theta_0-thin target support) is a possible escape at the bottom of every window.
Correct statement: "... needs fresh kind-(iv) groups whose data-direction switching is carried by SHARED SUPPORT targets of
mass >~ K_* t^2/H(L) at the active scales, by outside switching at shared coordinates, or by other switching strict
non-peaks".  Tiny shared target support is not a TS generator, so the tuning-lever duality (G3 4.4) does not cover it.
[In the method these rows are banked/raised S_th target rows, CUSHIONED (G1 Lemma 2.1(a)); so G-THIN does not create a
new residual -- it removes the claimed localization.]

## C. Construction (G3 Section 4)

C.1 Lemmas 2.1, 2.2: PROVED as abstract lemmas (part 3).
C.2 GAP G-NU (application of Lemma 2.2 in the persistence sketch of RC_L; precision to a SKETCH).  Computation (diagonal base,
nu = (sum_r (mu*_r)^2 a_r^2)^{1/2}, so d nu/d a_{s*} = (mu*_{s*})^2 a_{s*}/nu, and zhat_s = z_s + (mu*_s)^2 a_s/nu; zhat is invariant
under a -> c a since (mu*_s)^2 (c a_s)/(c nu) = (mu*_s)^2 a_s/nu):
      d zhat_s/d a_{s*} = -(mu*_s)^2 a_s (mu*_{s*})^2 a_{s*}/nu^3   (s != s*),   d zhat_{s*}/d a_{s*} = ((mu*_{s*})^2/nu)(1 - (mu*_{s*})^2 a_{s*}^2/nu^2).
So moving a tuning mass a_{s*} moves the Hilbert part of EVERY support coordinate s by the factor (mu*_s)^2 |a_s| |a_{s*}|/nu^2
(e.g. |a_{s*}|/|a_s| if s dominates nu) times its own effect.  Write theta_L for the stage-L tuning parameter (range R_L of
a_{s*(L)}), m_L(s) for the coefficient of zhat_s in the stage-L minor M_L, c_L ~ |m_L(s*(L))| (mu*_{s*(L)})^2 R_L/nu (own effect)
and H_L := sum_s m_L(s) (mu*_s)^2 a_s/nu (the Hilbert part of M_L, over ALL support coordinates in the pair's supports).  Then
      eps_{LL'} = c_{L'} kappa_{LL'},  kappa_{LL'} = |a_{s*(L')}| |H_L|/(nu |m_{L'}(s*(L'))|),   Lambda_{L'} >= sum_{L<L'} c_L kappa_{L'L},
and the weight conditions of Lemma 2.2 force, at L' = L + 1, kappa_{L,L+1} Lambda_{L+1} <= c_L/16 (from w_L/w_{L+1} >= 4 Lambda_{L+1}/c_{L+1}).
(a) If H_L has a part NOT proportional to c_L -- a coarse thick coordinate, or thin support whose Hilbert part is not small
compared with c_L (the depth of s*(L), hence c_L, is chosen by the adversary) -- then kappa_{L,L+1} and kappa_{L+1,1} are O(1),
Lambda_{L+1} >= c_1 kappa_{L+1,1}, and the condition O(1) c_1 <= c_L/16 FAILS for large L.  (b) In the pure product case
(H_L proportional to c_L) the conditions hold with geometric weights if c_L decays super-exponentially.  G3's "plausible, not
checked" needs this case distinction.  REPAIR (SKETCH): the
nu-coupling has rank one; fix nu as a parameter, solve the remaining triangular system (only direct-support couplings, avoidable by
placement) by Lemma 2.2, then solve the scalar equation nu = ||U^* a(theta(nu))|| by the intermediate value theorem; zhat is
invariant under scaling of a, so the normalization q*(a) = 1 is applied last.  This is an additional unverified point (v) of RC_L.
C.3 Lemma 2.3: PROVED; tail constant (1 + max mu*) and S_l ∩ T(l) = {} (min S_l = 3 * 2^l > l).
C.4 Cor. 2.4: the decomposition and the exact cancellation are PROVED; general fact: for any coordinate j outside the private
supports, det[[u_+(j), u_+(zhat)], [u_-(j), u_-(zhat)]] does not depend on zhat_j (also at a FREE j).  The "discrete coincidence"
conclusion is conditional on BOTH the free-lever SKETCH (type-(b) free coordinates with eta v >= Des^C x are levers excluded by
(R1)) and (D-pat) (label fix).  (D-pat) remains HEURISTIC: the pattern set depends on the window through x'_max; the
heuristic count (2^{K_L} patterns, typical distance 2^{-K_L} ~ (x'_max)^{1/2^l} >> x) is plausible; it must hold at EVERY clean
sub-window of every stage (countably many design conditions; e.g. Borel-Cantelli over random signature weights), not done.
C.5 GAP G-RCL (RC_L is obsolete as an adversarial target).  RC_L and (C3) rest on a wrong-signed tiny minor of the (X3) row and
the row of a common target CONTACT j.  G1 Cor. 5.4 (refereed correct mod chain) shows this configuration does not obstruct:
P^nat banks j, (X1-c)_j is cushioned, the minor is SOFT, l_+- are banded; G1 names "G3 (C3)" explicitly.  A persistent
residual row must be built on STRICT resonances (R-S1) (minors of one (X3) row and FR rows at FREE shared targets with robust
room), (R-S2), (R-S3), (R-L) or (R0^str), and -- by R-ESC.2 -- its active groups need an escape (shared support target,
outside switching, other active strict non-peaks).  N3 shows the resulting norm-level picture: with a shared support target the
strict FR minor governs activity (two-regime); without one the pair is pinned even at an exact resonance.
C.6 Lemma 2.6, Cor. 2.7: PROVED (2.7 conditional, as labelled).

## D. Other means (G3 Section 5)

D.1 Lemma 3.1, Cor. 3.2: PROVED.  (ii): Fort's theorem on the complete metric space S_{p*} (usc, compact values by global
compactness); at an lsc point Bishop-Phelps NA rows f_n -> f carry mates g_n -> g and (f_n, g_n) attains its norm.
D.2 PRECISION P-33 (Prop. 3.3 and "THE OBSTRUCTION").  Arithmetic correct.  Scope: for CONTACT minors (Lemma 1.7) the tolerance
at the companion is the bank cushion 2 theta_min/t of G1 Lemma 2.1(a) (violation <= 4|a^#_j|/t allowed), far larger than the VT
tolerance, and Mj is not moved by the bank at j (Cor. 2.4); the obstruction is moot there (G1 Cor. 5.4).  It applies to STRICT
FR minors, whose tolerance is (VT') (mass <= delta s_1/(64 rho), G1 Lemma 2.1(c)); this agrees with G1's remark that softening
FR rows needs banks >~ b/T.  "the minor is >= c r even if Mj(f) = 0" needs a robust cofactor and no cancellation (H2-ref P-52).
D.3 Scale dichotomy (SKETCH; label honest).  Slip P-53: a window with s_2 <= c delta |M|/C_f exists at stage L iff
|M| >= C_f s_2^min(L)/(c delta), so the persistence condition reads |M_L(f)| < C_f s_2^min(L)/(c delta) (not c delta T_lo/C_f).
Part (i) never applies with the current preparation (bias >> VT tolerance), so in practice only (ii) is available.
D.4 PRECISION P-34 (Lemma 3.4).  The computation is correct for the stated robust-spread move: q*(a + u a_p e_p) =
1 + u|a_p|(1 + O(mu*_p)), so |a'_p - a_p| = u|a_p|(1 - |a_p|)(1 + O(u + mu*_p)) and ||U^*(a' - a)|| >= mu*_p |a'_p - a_p|.  The
general sentence "no pre-modification of f that breaks an (R0) resonance is invisible to the window data" is not proved
(only one move is analysed; the conclusion concerns the raise-transfer error bound, a property of the tool): HEURISTIC.
D.5 Section 5.5 assessments: labels honest.

## E. Section 6 ((Q*)) and Section 8
(Q*) is correctly stated as a property of the method; after G-RCL and P-33 it should be restricted to STRICT resonances.  The
"norm-level reading" should read "support of mass >~ K_* P t^2 at the relevant scale" for "thick support" (G-THIN).  Bottom line
of G3 (no persistent residual constructed; no counterexample; (LSC-trunc)_N and density OPEN) is correct.

## F. Most valuable idea (referee's view)
G3's switching inequality (Theorem 2.10): the block's d-row combined with the SUMMED sign constraints at the shared coordinates
gives a minor-free inequality.  Sharpened (Lemma R-ESC): whether a group of strict non-peaks of an unshifted block can switch is
decided by CUSHIONS -- shared support, anti-aligned private support -- and by outside switching, never by the size of minors;
an exact resonance without an escape is pinned.  Hence a residual strict resonance (R-S1) needs BOTH a tiny strict minor AND an
escape at every large stage.

## G. Open (precise)
(1) (LSC-trunc)_N for every f; density of NA((c_0, p_N), l_2^2) for any N; density of NA((c_0, p), l_2^2) for the Martin-type p.
(2) The residual after G1/G1-ref, refined by R-ESC: at every clean sub-window and class of all large main stages, (R-S1) groups
    with a tiny wrong-signed strict minor AND an escape (shared support target of mass >~ K_* t^2/H(L), outside switching at a shared
    coordinate, or other active strict non-peaks), or (R-S2), (R-S3), (R-L), (R0^str).
(3) Method-level use of R-ESC.2 (threshold-gap bookkeeping in K1's classes).
(4) An explicit persistent residual row: RC_L re-targeted to (R-S1) with an escape; persistence needs G-NU's rank-one reduction
    and G3's points (i)-(iv).
(5) Scale dichotomy as a theorem (absolute-error class in the transport theorem); (Q*) for strict resonances; (D-pat) and the
    free-lever SKETCH of Cor. 2.4.
