# R3 referee, part 3: the rigid design (R3 4.5) and Model N with EC; the Hilbert-capacity gap

## 3.1 Model N numbers: REPRODUCED.
ec_modelN.py (a0 = 0.03, delta = 1; resource errors carried to tau_gen, frozen error to tau_F = tau_gen^2):
R = 1.0882, 1.0228, 1.0054 at tau_gen = 2^2, 2^3, 2^4 (R3: 1.088/1.023/1.005). Variant "frozen error absorbed above
tau_gen": 1.194, 1.155, 1.087 (slower). ec_onetype.py (one shift, one carrier): no EC 3.406; EC at 2^4, 2^6, 2^8:
R = 1.1682, 1.0406, 1.0089 (R3: 1.168/1.041/1.009). Modelling of EC (A := 0 below tau_gen, eta := 0 below tau_F) matches
the room lemma (tau_F = tau_gen^2/lambda_b) and the scaling Q_S -> 0 of part 2.

## 3.2 The Hilbert-capacity gap (NEW; NUMERICAL in Model N, with a rigorous mechanism). Claim 9/10's "one converted carrier
of one type (one global scalar) suffices" is NOT general; it is a borderline artefact of the parameters A = 1, B = 1/2.
Mechanism (PROVED at the level of the decomposition bounds, cf. part 2.2(b),(c)). Below the band (|t| << delta lambda_b)
the only carriers that can take the O(1) switching component two-sidedly at f'' are converted carriers: matched coarse
peaks have relative first-order cost delta Phi M/(m C |t|) -> infinity (4.7), destroyed ones likewise (|rho| ~ s/lambda,
cost ~ a0 s/tau), and EC generic carriers cannot take O(1) components (their frozen error eps_n >> lambda_b: the implant
scale gap, which R3 itself states). With N converted carriers and equal split, the block coefficient of the band
certificate is rho^2 S^2/(N m0^2 C''), so (HC) needs N >= rho^2 S^2/(m0^2 C'' Q). EC does not change this number.
Model N tests (refwork/onetype_A.py, twotype_A.py, bottom_hilbert2.py, supf_scan.py, coupled*.py):
 * Exact bottom value: P_{f'}(tau -> 0) = B S^2 / n_conv (n_conv = 2,4,...,16 checked: 0.25, 0.125, ..., 0.03125).
   R3's one-carrier case: B S^2 / sup P_f = 0.5/0.5225 = 0.957 (barely < 1).
 * Same scheme as R3 (one shift, one carrier, EC at tau_gen = 2^6): A = 0.5 -> R = 1.463; A = 0.25 -> R = 2.074;
   A = 1, B = 0.6 -> R = 1.086. Maximum at tau = 2^-8 (bottom), INDEPENDENT of tau_gen. All these are still "error-
   dominated" in E's sense (error weight >> peak weight a0 = 0.03), i.e. inside the class of E 7.3 (A1).
 * Both types converted by one group scalar (2 carriers), EC at 2^4: A = 0.5 -> 1.003; A = 0.25 -> 1.037; A = 0.1 -> 1.426.
 * Needed n_conv >= B S^2/sup P_f grows like log(1/c) when the linear costs c = (A, a0) -> 0 with delta fixed:
   0.96, 1.46, 2.85, 3.21, 4.84, 6.38, 8.12 (c from (1, 0.03) to (0.003, 0.0003)).
 * Model N treats a0 and delta as independent; in the real norm the peak cost is tied to the margin (4.7: alpha = delta Phi^2 M/C),
   and smaller delta widens the conversion band ((2+delta)/delta). With a0 (1+delta) = delta (coupled model): bottom ratio with
   ONE shift = 0.29-0.83 (delta = 1 ... 0.03), i.e. the bottom is met; but the full profile with one shift and A = 0.1 delta,
   delta = 1 gives R = 1.090 at tau ~ 4.7 (boundary layer a few octaves above the band) for tau_gen = 2^6 AND 2^8
   (no decay: this excess is a Hilbert/room deficit, not an error cost); delta = 0.3: R = 1.035 (2^6), 1.024 (2^8, max at
   tau ~ 18). With TWO shifts (both types converted): R = 1.0000.
Conclusion. EC removes the ERROR-driven conversion requirement (J ~ 32 kappa/(1-rho^2)); it does not remove a
rho-independent HILBERT/ROOM-capacity requirement: the converted carriers near the band must replace the room of the
destroyed ones (about sum_{destroyed} 2M lambda_i / t ~ 4 M lambda_b/t at scale t) and carry S below the band with block
coefficient <= Q. In E's strongly error-dominated regime (A large relative to B) EC compensates the deficit (f'' saves f's
error costs); otherwise a bounded number of conversions (both types, sometimes more) is still needed. So:
 - "one converted band carrier (one global scalar suffices)" (claim 9): FALSE as a general statement, even inside E's
   class (A1)-(A5); TRUE in Model N only when B S^2 <= sup P_f and the boundary-layer deficit is compensated;
 - "bounded conversion capacity is not an obstruction for compact errors" (headline): must be weakened to "the
   error-driven part disappears; a bounded, rho-independent Hilbert-capacity requirement remains";
 - "E 8.3's conversion-capacity bound is irrelevant": overstated; it is irrelevant for the error part only.
Whether E-type designs can make the Hilbert-capacity requirement exceed the conversion capacity available at group
transitions (two group scalars + V) is OPEN; in the coupled model two shifts sufficed in every case tested.

## 3.3 Other issues in the 4.5 sketch (fixable).
P1 (protected set, inconsistent as written). 4.5(1) takes Pi = {v, finitely many designated carriers} and 4.5(3) re-solves
"protected against the band carriers". A designated/band carrier is u ~ (v + K lambda sigma + ...)/n with sigma in E_c; with v
protected, protecting u protects sigma|_G, and by Remark 2.2(2) hypothesis (ii) then FAILS as soon as the protected sigma|_G and
v|_G span a target direction (e.g. once dim E_c matched carriers with spanning sigma's are protected); if the span is only
approximate (sigma_band(zhat) = O(1/K) != 0), beta blows up instead (harmless for EC, eps_n is free, but T_n and tau_F shrink).
The affected directions are those of the frozen errors that EC is meant to carry. Fix: protect only v (this is necessary: a
change of v(x'') shifts a carrier at depth lambda by the relative amount v(eta)/(theta lambda), huge near the band). Statuses of
the carriers are then preserved without protection: a window move eta with v(eta) = 0 shifts every v-carrier by
K lambda_k sigma_k(eta)/n_k, a relative shift O(K ||sigma||_1 ||eta||_inf/theta) uniformly in k, and ||eta|| <= 1/(2n) -> 0
(the induced change of |zeta''| is first order (L*w'')(eta) = O(||eta||): a uniform rescaling of thresholds).
P2 (order of choices). Theorem EC fixes x'_{N(n)} and the move; the boundary (far contacts, destroyed groups) and the contact
masses come later and change u_{k_{n,i}}(x'') through far tails (up to 2 ||u_k - b_i||_1 <= 2 eps_n if b_i lives on the window;
this may be >> Phi(k), the actual depth being chosen by T) and through e''. The EC system must therefore be re-solved LAST
(same eta_l, same matrix A_n, right side O(eps_n + ||U|| ||Delta e''||), move O(beta eps_n) -> 0). R3 does re-solve; its extra
argument "contact masses change e'' by O(T_0 theta lambda_b) << theta Phi_gen" is then unnecessary.
P3 (EC moves are chosen before the boundary). The final EC move has size ~ beta eps_n, fixed before lambda_b, so it shifts every
block coordinate k by u_k(eta). For the switching carriers this is harmless (window part v + O(lambda), v protected, see P1).
For OTHER structure of f at depth ~ lambda_b (peaks of other directions, other blocks) nothing controls u_k(eta) relative to
Phi(k): their statuses may change (E 8.1). This is part of what (HT-EC) has to absorb and should be listed with it.
P4 (detector errors, contacts). Correct in outline: detector parts of the band's frozen error are O(lambda_b) (destruction
needs delta_k ||psi|| ~ Phi_k), masses ~ T_0 lambda_b = o(1), Hilbert cost O(t^2 lambda_b^2). The single-coordinate case:
R3 says s_{n_b} in {1 - z_j, -1 - z_j}; that is only if the coordinate must be a contact. By 4.4 with r = 1 the one coordinate
may stay fractional (any value of s_{n_b}), at the price of one-sided first-order absorption of its detector error.
P5 (zhat-components). Errors must lie in xihat''-perp to be carried (u_k(x'') = 0 on S); the component along a vector with
value 1 at xihat'' has to go into the normalisation/d-terms; SKETCH, agreed.
P6 ((HT-EC)). Unproved, acknowledged. My bookkeeping of what it contains: at f the destroyed carriers carry, at every scale
t >= lambda_b, an ABSOLUTE amount <= sum_{lambda_i < lambda_b} 2 M lambda_i ~ 4 M lambda_b of t S v (room bound). At f'' this
amount must be re-routed (to matched carriers at depth ~ t: extra error K lambda_b sigma, constant in t, carriable by EC up to
tau_F; extra Hilbert ~ 2 x Delta x/(m^2 C) with Delta x ~ lambda_b/t: NOT carriable by EC) or replaced by converted band
carriers (room M lambda_b/t each, zero error). This is the Hilbert/room deficit of 3.2. So (HT-EC) is not only "transport
of matched structure"; it contains the capacity count of 3.2.

## 3.4 Verdict on claim 9 (rigid design recovered).
SKETCH label appropriate, but the sketch has a gap besides (HT-EC): the Hilbert/room capacity of the converted carriers.
With P1-P5 fixed and the hypothesis "the converted carriers near the band have enough room/Hilbert capacity" ADDED, the
recovery modulo (HT-EC) is plausible (Model N supports it in the tested cases with both types converted).
