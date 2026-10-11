ERRATUM (see G3_notes.md, authoritative): the numerics entry 'D = -0.004 (right sign), THICK r: FREE' was computed before the
peak-carrier fix; after the fix l_- is a PEAK in that configuration (pinned, outside Lemma 2.8).  The right-sign test is D = -1e-3
(free).  Lemma 3.4 is restated in the notes with a footprint bound (PROVED mod chain).

# G3 part 3: recovery "by other means" at residual rows; the precise quantitative property; numerics

Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  Notation of parts 1-2.

## 3.1 Non-recoverability is an open condition on the graph (method-independent)

Let G := {(f, g) : f in S_{p*}, g in C(f)} (closed in X* x X*: Lemma 2.6) and Rec_pairs := G ∩ cl NA((c_0, p), l_2^2).

LEMMA 3.1 (openness).  PROVED.  If (f, h) is contractive and (f, h) notin cl NA, there is delta > 0 such that every contractive
(f', h') with ||(f', h') - (f, h)|| < delta is notin cl NA.  In particular, if (f, rho g) notin cl NA then for every row f' with
p*(f' - f) < delta/2 that lies in Rec (every mate of f' is recovered),
      dist(rho g, C(f')) >= delta/2.
Proof.  cl NA is closed: B((f, h), delta) ∩ NA = {} for some delta; if (f', h') in cl NA were within delta/2 of (f, h), an NA operator
within delta/2 of (f', h') would lie in B((f, h), delta).  For f' in Rec and g' in C(f') with p*(g' - rho g) < delta/2, (f', g') is in
cl NA and within delta of (f, rho g) [operator norm <= p*(f'-f) + p*(g'-rho g)], a contradiction.  QED
COROLLARY 3.2 (what a counterexample must defeat).  PROVED.  A non-recovered (f, rho g) must stay delta/2-far from the fibres of ALL
rows near f in: (i) the rows with finite base support (Master Theorem VI); (ii) the comeager set Omega of points of lower
semicontinuity of the fibre map (Fort's theorem: f -> C(f) is upper semicontinuous with compact values by Lemma 2.6 and global
compactness, S_{p*} is complete; at f in Omega, every g in C(f) is a limit of mates of NA rows, so Omega ⊂ Rec); (iii) every row covered
by the transport theorem, in particular every row at which the residual fails at infinitely many main stages.  Consequently a
counterexample built on a persistent residual row f needs the residual to persist on a whole NEIGHBOURHOOD of f in the sense that
every row f' near f carrying mates near rho g is again a persistent residual row.  A codimension-one coincidence at each stage does
not have this property unless the mates themselves force it.  This is the strongest structural argument against a counterexample
that I can make rigorous: it does not exclude one, because the mates near rho g may exist only at rows satisfying the same
coincidences (Lemma 1.7 shows that wrong-signed minors pin mates, so mates near rho g can indeed force structure on f').

## 3.2 The window restricted to the free regime, and why it is blocked (precise)

PROPOSITION 3.3 (a wrong-signed minor is harmless above its pinning scale).  PROVED (conditional on the engineered-approximant
machinery with window bottom s_1', i.e. Lemma VT of U3/X2 and Theorem UE^inf, as stated in Part III).  In the configuration of
Lemma 1.7, suppose the exact data at the companion are taken with the pair active and the contact row at j NOT exactified (Mj != 0).
Then the side violation at j is |V_j| = |gamma_1| |Mj|/|u_2(zhat)| (up to the O(S) term), an l_1-violation of mass
eps_j <= C_d |Mj| (C_d := A_max/|u_2(zhat)|, A_max the data bound).  Lemma VT tolerates it iff 2 rho eps_j <= delta s_1'/16, i.e. iff the
window bottom satisfies
      s_1' >= 32 rho C_d |Mj| / delta.                                                                     (3.1)
So a window whose smallest scale is >= C|Mj| needs NO exactification of the minor Mj.  By Corollary 1.8 the pair switches with order-
one amplitude only at scales >~ |Mj|, so the restriction (3.1) removes only the scales at which the pair is pinned anyway.
Proof.  The violation computation is Lemma 1.7(ii) with exact data (S = 0 at the companion, psi_j = 0).  The tolerance criterion is
Lemma VT verbatim.  QED
THE OBSTRUCTION (PROVED as a chain of the cited design inequalities).  The construction of Part III requires
 (L-K2-1)  s_1 <= theta_0 T/(8 rho A_0),   theta_0 = b/Design^{C_P}        (K2 (K2-d), H2-ref F-NE),
because the Sys-DC levers must be two-sided at the scale r >= 16 K_J Pi_X (Pi_X the Hilbert footprint of the window masses) and, for
kind-(iv) carriers, two-sidedness comes from preparation banks of base mass theta_0 with theta_0 eff >= r.  Wrong-signed minors with
|Mj| in (b T/(Des^C), C b] therefore violate (3.1) for every admissible s_1.  Moreover the preparation BIAS (H2 Lemma 5.2) raises
every banked kind-(iv) value by theta_0 eff v >= r, so at the prepared row the minor is >= c r even if Mj(f) = 0; and r >= 16 K_J Pi_X
while (3.1) needs |M| <= delta s_1/(32 rho C_d): the ratio bias/tolerance is >= 512 rho C_d K_J Pi_X/(delta s_1), a fixed large factor
(Pi_X >= c s_1 when window masses sit at near coordinates, Lemma III-masses (iv)).
QUANTITATIVE PROPERTY (Q*) whose failure at every stage a persistent (R1) row needs:
      bias(Sys-DC levers on the resonant rows) + |lambda^T M(f)|  <=  delta s_1^{VT}/(32 rho C_d),
with s_1^{VT} the window bottom used by Lemma VT, compatibly with the lever-scale requirement r(s_1^{VT}) of Sys-DC.
Equivalently: the minimum, over two-sided d-consistency levers for the resonant kind-(iv) rows, of (lever bias)/(lever range) must be
<= delta/(512 rho C_d K_J) -- i.e. BIAS-FREE two-sided levers for fully swallowed kind-(iv) carriers (H2 5.3, G2 Theorem ML: a pullable
coordinate in [cap_min/2, c_0 W] gives one).  (Q*) fails exactly at "deep-swallowed" carriers (G2 Theorem 4.9).
[This is consistent with G2's Proposition 4.7: even EXACT resonances obstruct, because the obstruction lives at the error scale of
the realization (the bias), not at the size of the resonance.]

## 3.3 The stable-exact flat direction and invisible modifications (R0): heavy thick masses

LEMMA 3.4 (thick masses are heavy).  PROVED (from K2.16(4) and the definitions).  At an (R0) stage the thick private coordinates p of a
thick-type carrier have |a_p| >= u(w)/2 (after the deep-raise normalization, which changes masses by a factor in [1/2, 2]); a
relative change of a_p by a factor (1 + u) (the move that creates robust spread, K2.17(e), and destroys every near-certificate)
moves the row by >= u(w)^2/4 in norm and its Hilbert footprint by >= mu*_p u(w)^2/4 >= u(w)^2/(4 Design(L)^{1/2}), which exceeds
s_1(w)^2 by an astronomical factor.  Hence a pre-modification of f that breaks the (R0) resonance and is invisible to the window data
(transfer error << s_1^2) does not exist; the stable-exact direction Phi_0 (p*(f + t Phi_0) <= 1 + C t^2) moves the thick support only
at second order, i.e. by O(t^2) at scale t, and cannot be used as such a modification either.
Proof.  K2.16(4): |kappa a_s| >= c_* u/(2 nu_1) at thick coordinates and thickness means |a_s| >= u/2 by definition (J1 1).  The norm of a
base change Delta a is >= ||Delta a||_1 - ||U^* Delta a|| >= (1 - mu*_p)|Delta a_p|; the footprint is mu*_p |Delta a_p| with
(mu*_p)^2 >= 1/Design(L) at design depth (K2 1: Design(L) >= ... /(mu*_{D(L)})^2); s_1 <= u T is far below u^2/Design^{1/2}.  For Phi_0:
f + t Phi_0 = a + L^*(w + t rho~) has the same base vector, and its normalization changes the base by O(t^2).  QED
So "other means" for (R0) cannot be a cheap pre-modification; they would have to use Phi_0 inside the companion, which is J1's gauge
(7.3, SKETCH) -- not pursued here.

## 3.4 Raise transfer with a different companion, Theorem N, transitivity (assessment)

- Raise transfer (V3 Lemma 2.3) moves only same-sign masses; its error terms 2||U^* Delta a|| + p*(L^*(w^# - w)) are constants, so a
  raise transfers mates exactly only above the scale (error)^{1/2}; resonances live in the Hilbert/sign data of design-depth or
  target coordinates (Lemma 2.3), which raises move by at most their footprint.  A raise cannot change the SIGN data that fix a
  wrong-signed private resonance (Corollary 2.4), and changes thick-target Hilbert data only with a two-sided effect that the
  certificate annihilates (tuning-lever duality).  No relief.  (HEURISTIC with PROVED ingredients.)
- Theorem N (box-dominated support) needs F = N and Bx <= C_a |a| with a margin rate; a persistent (R1) row has thin (<= b) support
  off the targets at every stage (C1), so its box ratios are unbounded unless the mate's boxes are thinner still; not applicable to the
  dangerous mates (whose switching lives on contacts).  (HEURISTIC.)
- Transitivity (Lemma 3.1, Corollary 2.7 remark): the natural dangerous mates are limits of mates of exactly-resonant rows; those
  rows are bias-type residual (H2 Lemma 5.2, G2 Prop. 4.7), so transitivity gives nothing new.  (PROVED as stated.)

## 3.5 Numerics (sanity only; r14/G3_work/)

model.py: finite one-block Martin-type norm (base q*(A) = ||A||_1 + ||mu A||_2, block N(W) = ||W||_inf + ||Phi W||_2), forced data of
f[a, z], p*(.) by SOCP, and max_switch(t, k): the maximum of the switching amplitude gamma'_k over g with g(xi) = 0 and decompositions of
f +- t g with norms <= s(t) (exactly the quantity bounded by Lemmas 1.5-1.7, 2.8).  Solver CLARABEL (cvxpy 1.9).
selfpin.py / selfpin.out: pair l_+ (eps = +1), l_- (eps = -1) of STRICT NON-PEAKS (checked: peaks = {2, 3, 4}) sharing the contact j;
peaks with private contacts of both orientations ((P1)); p*(f) = 1.00000000 in every case.  max gamma'_+ / t at t = 0.1, 0.03, 0.01:
   D > 0 robust (2.05e-3), anti-aligned mass 0:         18.0, 20.6, 20.6      pinned by the contact j (Lemma 2.8(c))
   D = 0 via an anti-aligned CONTACT r:                 13.7, 13.8, 13.9      pinned by r (Lemma 2.8(e), Cor. 2.9)
   D = 0 via anti-aligned THIN support a_r = 1e-4:      14.3, 21.2, 80.4      pinned above the cushion scale, relieved below
   D = 0 via anti-aligned THIN support a_r = 1e-3:      20.3, 58.9, 166       relief starts at larger scales (bigger cushion)
   D = 0 via anti-aligned THICK support a_r = 0.15:     20.3, 59.1, 166       FREE: max gamma'_+ ~ 1.66-2.03 at all scales
   D = -0.004 (right sign), THICK r:                    22.7, 73.6, 218       FREE
(values at t <= 3e-3 are flagged "optimal_inaccurate": the excess budget s(t) - 1 ~ t^2/2 is then at the solver tolerance).
tworegime.py / tworegime.out (thick anti-aligned r, peaks pinned two-sidedly): D = 1e-3 (wrong sign): max gamma'_+/t = 41.1, 41.1 at
t = 0.03, 0.01 (Lemma 2.8(c) slope |val_-|/(2 q_0 D) = 33.3 plus the O(S_0) terms): PINNED; D = 1e-4: max gamma'_+ = 1.85, 1.74 at
t = 0.03, 0.01 (free regime, t >> D) and decreasing (1.49, 1.06) at t = 1e-3, 3e-4 (approaching the pinned regime; inaccurate
solves); D = 0 and D = -1e-4: free (1.76-1.89 at the accurate scales).  The two-regime profile of Corollary 1.8 is visible.
Conclusion of the numerics: consistent with Lemmas 1.5-1.7, 2.8 and Corollary 1.8 at the scales where the solver is accurate; they
prove nothing about the infinite-dimensional questions.
