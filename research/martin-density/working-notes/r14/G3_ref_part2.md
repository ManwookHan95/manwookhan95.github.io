# G3-ref part 2: Section 3 of G3 (unshifted blocks) -- Theorem 2.10, Cor 2.11, Lemma 2.8, Cor 2.9, Interpretation

## Verdicts
- Theorem 2.10: correct for ANY set J_c (contacts, free, support; cushion 2 alpha(J_c)/t).  Identity
  Rt_k = sum_{s notin J_c} u_k(s) zhat_s + sum_{J_c} u_k(j) h_j re-derived.  Numerically verified (N1, random G and J_c).
- Cor 2.11: correct.  Case split P_k = N^z + F^z + Fr (Fr over all free coordinates) re-derived; case (3):
  eps Rt_k >= N^z - F^z - h_k because Rt_k = sum_{private} u_k(s) z_s + sum_{supp} u_k(s) h_s; |Rt_k| <= P_k + h_k <= 5P_k/4.
  SHARPENING (proved in ref notes, Lemma R-ESC): only the cushions of the ANTI-ALIGNED private coordinates (case (1))
  and of J_c (through E(t)) enter; ALIGNED private cushions never enter.  Hence the data-direction switching of a group of
  kind-(iv) carriers (near coordinates aligned by definition of the data sign) with small far mass (deep-swallowed) is
  pinned at O(t) with design constants at EVERY scale, unless the group has shared support coordinates (cushion
  2 alpha(J_c)/t), outside switching at shared coordinates (Psi_J), other switching strict non-peaks (r_Q), or (P1) fails.
- Lemma 2.8 (a)-(e): correct (identity A val_- - B val_+ = D re-derived; (d) by D >= v_0 (w_+ + w_-)).
- Cor 2.9: correct as an inequality, but its constant C_v [ ... + S_0/v_0 ] depends on the f-data v_0 = min(val_+, |val_-|)
  and C_v = max(1, val_+/|val_-|, |val_-|/val_+): NOT design-controlled for nearly-zero-valued carriers (P-29).  The
  design-controlled statement of Interpretation (a) is nevertheless TRUE, via Cor 2.11 (whose constant has no v_0).
- Interpretation (a): correct (via 2.11; above the anti-aligned cushion scale).
- Interpretation (b): the list of escapes is correct; the final sentence ("Persistent (R1) ... therefore needs fresh
  kind-(iv) rows switching through shared THICK target support") does not follow: it drops the escape it lists
  ("thin support below its cushion scale"), which at window scales is the generic case (G-THIN below).

## G-THIN (gap in Interpretation (b), Section 6 norm-level reading, RC_L)
Window bottoms satisfy s_1 <= theta_0 T/(8 rho A_0) << theta_0 = b/Des^{C_P} <= b ((L-K2-1), H2-ref F-NE).  A shared
support coordinate s of f with mass |a_s| relieves the group at scales t <~ (|a_s|/(K_* P))^{1/2} (relative activity)
or t <~ |a_s|/P (order-one activity).  So a b-thin (even a theta_0-thin) shared target coordinate is an escape at the
bottom of every window; "thick" in the conclusion must be read relative to the window scale (|a_s| >~ K_* P s_1^2), not
as |a_s| >= u(w)/2.  Consequences: RC_L does not need THICK shared targets; and the tuning-lever duality of 4.4 (which
uses that thick targets are TWO-SIDED TS generators annihilated by every near-certificate) does not cover tiny shared
target support, which after the preparation is S_th (one-sided, K2.16(2c)).  [Per G1, tiny-support/banked target rows are
cushioned (soft) in the method; so this escape is handled by G1's soft transplant, and the residual remains at strict
rows.  The point is that G3's norm-level localization "switching only through shared THICK targets" is wrong at window
scales.]

## Numerics N2 (r14/G3_ref_work/test_pin.py, test_pin2.py; outputs test_pin_deepfar.out, test_pin2.out, test_pin2b.out)
One unshifted block (peaks {2,3,4}, peak carrier with private contacts of both orientations), pair l_+ (eps=+1), l_- (eps=-1)
of strict non-peaks sharing ONE coordinate j, disjoint private supports: near coordinates of the data sign (mass 0.3),
far anti-sign contacts of mass 1e-4 (deep-swallowed type).  max gamma'_+ (data direction) / t:
  (ii)  j contact, near contacts:                  1.27, 1.27, 1.27, 1.27  (t = .1, .03, .01, .003)     pinned
  (i)   j contact, near THIN support a = 1e-3:     2.1, 6.3, 6.3, 6.3                                   pinned at ALL t
        (anti-data direction: 2.1, 8.9, 69, 304 -> order one: near cushion relieves only the anti-data direction)
  (iii) j THIN shared support a_j = 1e-3:          2.0, 9.7, 41, 299 (gamma'_+ = 0.90 at t = .003)      RELIEVED (G-THIN)
  (iv)  j FREE (robust FR minor), near thin:       4.4, 13.3, 13.4, 13.4                                pinned at ALL t
  (vi)  j FREE, EXACT FR resonance, near contacts: 2.25 at every t                                      pinned (minor 0!)
  (v)   j FREE, EXACT FR resonance, near thin:     3.7, 18.4, 134 -> order one                          relieved, with l_-
        switching AGAINST its near coordinates (both oriented values have the same sign at an exact FR resonance with
        aligned private parts: the kernel direction is data-direction for one carrier and anti-data for the other).
Reading: whether a pair switches is decided by CUSHIONS (shared support, anti-aligned private support), not by the
minor: an exact FR resonance with contact-only private coordinates is pinned (vi); a robust minor with a shared thin
target is relieved (iii).

## P-NUM (G3's own numerics)
G3's selfpin/tworegime/conserve model gives the pair two SHARED thick coordinates S0, S1 (same coefficient TP, signs
+1/-1) to make the values small; so Lemma 2.8's hypothesis E_+ ∩ E_- = {} fails in G3's model.  Lemma 2.8 (b), (c) are
identities/inequalities not needing disjointness and are validly tested; (a), (d), (e) and Cor 2.9/2.11 are tested only
because S0/S1 enter Rt_k with weight TP(h_S0 + h_S1) ~ 0 ("neutral" thick coordinates).  The reported numbers are
consistent with the bounds (e.g. D = 2.05e-3: bound ~ (9.0 + 27) t >= observed 20 t).  N2 above uses disjoint supports.

## Numerics N3 (r14/G3_ref_work/test_fr.py, test_fr_ctrl.py; outputs test_fr.out, test_fr_ctrl.out): strict FR resonance
with and without an escape.  Pair sharing a FREE target j (z_j = 0.3; strict FR row) and a second shared coordinate s;
private near = data-sign contacts, far = contacts of mass 1e-4; FR minor M tuned exactly.  max gamma'_+ at t = .1/.03/.01:
  shared THICK support s (a_s = .3):  M = 0: 1.39/1.38/1.38 (FREE);  M = 1e-3: 1.38/1.35/1.29;  M = 1e-2: 1.32/1.11/0.74
                                      (two-regime in |M|, Cor CL.2)
  shared THIN support s (a_s = 1e-3): 0.19/0.21/0.51 for M = 0, 1e-3, 1e-2 (relief only below the shared-cushion scale)
  shared CONTACT s (control):         0.113/0.034/0.011 for M = 0, 1e-3, 1e-2 (PINNED, slope 1.13, even at M = 0)
Check of Lemma R-ESC (1)-(3) term by term on 108 decompositions of the test_pin variants (check_resc.py/.out): worst
normalized slacks -5.8e-4, -1.3e-2, -8.3e-3 (all hold; (1) nearly tight).
