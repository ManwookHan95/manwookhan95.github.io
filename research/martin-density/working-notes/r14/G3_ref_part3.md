# G3-ref part 3: Sections 4-6 of G3 (construction, other means, (Q*))

## 4.1 Lemmas 2.1, 2.2: correct as abstract lemmas.
- 2.1: nested closed balls, d(x_{i+1}, x_i) < s_i/2, s_{i+1} <= s_i/4 => B_{i+1} ⊂ B_i; completeness.  Correct.
- 2.2: T maps B into [-3/4, 3/4]^N; completeness of (B, ||.||_w) (coordinatewise limit is the ||.||_w-limit);
  min_{L'<L} w_{L'} max_{L'<L}|Delta_{L'}| <= max_{L'<L} w_{L'}|Delta_{L'}| <= D_T; D_T <= D_T/4 + D/4.  Correct.
- APPLICATION to RC_L (G-NU, precision; RC_L is a SKETCH anyway).  The cross effects are NOT only "Hilbert footprints of
  the deeper coordinate": zhat_s = z_s + mu_s^2 a_s/nu with the GLOBAL nu = ||U^* a||, so
     d zhat_s / d a_{s*} = - mu_s^2 a_s mu_{s*}^2 a_{s*} / nu^3   (s != s*),   d zhat_{s*}/d a_{s*} = (mu_{s*}^2/nu)(1 - mu_{s*}^2 a_{s*}^2/nu^2),
  so a tuning coordinate moves the Hilbert part of EVERY thick coordinate by (a_{s*} mu_s^2 a_s/nu^2) times its own effect.
  If the stage-L minor's Hilbert part is proportional to its own effect c_L (pure product case), the weight conditions of
  Lemma 2.2 hold with geometric weights when c_L decays super-exponentially.  If it has a part NOT proportional to c_L (a COARSE
  thick coordinate, or thin support not small compared with c_L -- the adversary fixes c_L through the depth of s*(L)), the
  relative coupling is O(1) in both directions, the max-norm Lipschitz constant Lambda_{L'} >~ c_1 dominates, and the weight
  conditions FAIL for large L (precise form: ref notes C.2).  Repair (SKETCH): the nu-coupling has rank one -- fix nu as a
  parameter, solve the remaining (now directly coupled only) triangular system theta(nu) by Lemma 2.2, then solve the scalar
  equation nu = ||U^* a(theta(nu))|| by the intermediate value theorem (the tuning moves nu by doubly exponentially small
  amounts; zhat is invariant under scaling of a, so the normalization q*(a) = 1 is done last).

## 4.3 Lemma 2.3: correct; tail constant: |E_l| <= sum (mu*_s)^2 v_l(s)|a_s|/nu + (1 + max_s mu*_s) ||u_l 1_{(D',inf)}||_1
(|zhat_s| <= 1 + mu*_s).  S_l ∩ T(l) = {} because min S_l = 3 * 2^l > l (so the "counted in Y_l" clause of part 2 is vacuous).
## Cor 2.4: decomposition and the exact cancellation of the zhat_j terms are correct (general fact: the 2x2 minor of the
value row and the row at j does not depend on zhat_j; the same holds at a FREE j).  LABEL: the conclusion depends on the
free-lever SKETCH (type-(b) free coordinates with eta v >= Des^C x are levers excluded by (R1)) as well as on (D-pat).
Without the SKETCH, free type-(b) coordinates are continuous private tuning data and the "discrete coincidence"
conclusion fails.  Remark 2.5 (D-pat): HEURISTIC label honest; the pattern set grows as the window shrinks (type-(b)
coordinates down to x'_max; part 2 counts K_L ~ 2 log_2(tail/x'_max)/2^{l+1}); the sparsity of S_l makes the count
small, but (D-pat) must hold at EVERY clean sub-window of every stage -- a countable family of conditions on the design,
to be arranged (e.g. Borel-Cantelli over random signature weights with summable bad probabilities); not done.

## 4.5 RC_L (SKETCH) -- G-RCL: the configuration is OBSOLETE after G1.
RC_L rests on (C3): a wrong-signed tiny minor of the value (X3) row and the row of a common target CONTACT j.  G1 Cor. 5.4
(refereed correct mod chain, G1-ref) shows that this configuration does NOT obstruct: P^nat banks j, the row (X1-c)_j is
cushioned, the minor is SOFT (|M(rc)| <= (1 + 2 Lip) b << mu_tol).  G1's own text names "G3 (C3)" as realized.  So a
persistent residual row must be built on STRICT resonances (R-S1)/(R-S2) (minors of (X3) and FR rows at FREE shared targets
with robust room), (R-S3), (R-L) or (R0^str), not on RC_L.  Moreover (Lemma R-ESC, ref notes) an (R-S1) group of
kind-(iv) carriers of an unshifted block can be ACTIVE (|gamma| >> t) only with an escape: shared SUPPORT targets (soft
rows) of mass >~ K_* t^2/H(L), outside switching at shared coordinates, or other active strict non-peaks.
Additional unverified point (v) of the persistence sketch: the nu-coupling (G-NU).

## 4.6 Lemma 2.6, Cor 2.7, remark (transitivity): correct (Cor 2.7 conditional on the approximants, as labelled).

## 5.1 Lemma 3.1, Cor 3.2: correct.  Cor 3.2(ii): Fort's theorem (usc compact-valued multifunction on the complete metric
space S_{p*} is lsc on a comeager set); at an lsc point, Bishop-Phelps NA rows f_n -> f carry mates g_n -> g, and
(f_n, g_n) is norm attaining (f_n attains at x_n and ||(f_n(x_n), g_n(x_n))|| >= 1 >= ||(f_n, g_n)||).  [Known fact, cf.
BRIEFING (R3).]

## 5.2 Prop 3.3 and the obstruction: arithmetic correct (mod chain).  SCOPE (P-33): for CONTACT minors (Lemma 1.7) the
relevant tolerance at the companion is NOT (VT) but the bank cushion 2 theta_min/t of G1 Lemma 2.1(a) (far larger), and
the configuration is realized (G1 Cor 5.4); the obstruction "(3.1) fails for |Mj| in (b T/Des^C, C b]" is moot there.
It applies to STRICT FR minors, whose tolerance is (VT') (mass <= delta s_1/(64 rho), G1 Lemma 2.1(c)) -- consistent with
G1's remark that making FR rows soft would need banks >~ b/T.  "the minor is >= c r even if Mj(f) = 0" needs a robust
cofactor and no cancellation (H2-ref P-52), and for contact minors banks at j do not move Mj at all (Cor 2.4).

## 5.3 Scale dichotomy (SKETCH): label honest.  Slip: a window below c delta |M|/C_f exists at stage L iff
|M| >= C_f s_2^min(L)/(c delta); the persistence condition should read |M_L(f)| < C_f s_2^min(L)/(c delta) (G3 wrote
c delta T_lo/C_f).  Qualitatively unchanged.  Part (i) never applies with the current preparation (bias >> VT tolerance).

## 5.4 Lemma 3.4: the computation is correct for the stated move (a_p -> (1 + u) a_p): |a'_p - a_p| = u|a_p|(1 - |a_p|)
(1 + O(u + mu_p)), ||U^*(a' - a)|| >= mu_p |a'_p - a_p| >= c_0 u^2/(3 Des^{1/2}).  OVERCLAIM (P-34): "no pre-modification of
f that breaks an (R0) resonance is invisible" is proved only for this move; other resonance-breaking moves (z-moves,
block data, other masses) are not analysed, and the conclusion concerns the raise-transfer ERROR BOUND (a statement about
the tool), not the actual transfer of mates.  Downgrade the general sentence to HEURISTIC.  The Phi_0 remark refers to one
decomposition of f + t Phi_0, not necessarily its forced decomposition (minor).

## 6 (Q*) OPEN: correctly stated as a property of the method.  With G-RCL and P-33 it should be restricted to STRICT
resonances.  NORM-LEVEL READING: "paid ... by thick support, which at an (R1) stage lies only at shared target
coordinates" -> replace "thick" by "support of mass >~ K_* P t^2 at the relevant scale" (G-THIN); otherwise correct
(Lemma R-ESC: only SHARED support of the group, anti-aligned private support, outside switching or other strict non-peaks
can pay; private ALIGNED support never pays).
