# Z4 part 5: the model case (O3) — maximal contact

Setting: SLD (or SLD_G), N fixed, f with F finite and z ≡ eps_0 on N \ F (eps_0 in {±1}). Then K = N \ F, J = ∅, every carrier is
swallowed with eps_l = eps_0 (r_l = 0 for all l: Remark rem:Bpm(a)), B = L_N.

**Lemma 5.0 (peaks of both signs).** PROVED. In every block m there are infinitely many peaks k with w_m(k) = +M_m and infinitely many with
w_m(k) = -M_m, all with margins >= q_0/4 for k large.
*Proof.* q**(zhat) = 1, so there is y in S_{q*} with y(zhat) > 3/4; by (T-d) there are k -> infinity with q*(u_{k,m} - y) -> 0, hence
u_{k,m}(zhat) > 1/2 for those k (|v(zhat)| <= q*(v)); as Phi_m(k) -> 0, Lemma lem:threshold makes k a peak with w = +M and margin
mu = q_0(|u(zhat)| - hat theta Phi_m(k)) >= q_0/4 for large k (hat theta := |R**zhat| M/(mC) as in the proof of Lemma lem:scrambling). Use -y. QED.

**Proposition 5.1 (rigidity: two-piece data are d-neutral at maximal contact).** PROVED. Every two-piece data (b^±, omega^±) for a
functional g at f (Definition def:twopiece) satisfy Delta d_m := d_m(omega^-_m) - d_m(omega^+_m) = 0 for every m. Consequently the
non-negative mismatch allowed by Corollary cor:D1 is never available at maximal contact.
*Proof.* v := b^+ - b^- = sum_m R_m^*(delta omega_m - Delta d_m w_m), delta omega := omega^- - omega^+ (finitely supported in the Q_m), and
eps_0 v(j) >= 0 for every j notin F (sign conditions on K = N \ F). Fix m and, by Lemma 5.0, swallowed peaks l^± of block m with
w(k(l^±)) = ±M_m and S_{l^±} ∩ F = ∅. Let T_omega be the (finite) union of the target supports of the carriers in the supports of the
delta omega_{m'}. For s in S_{l^±} \ T_omega: the delta omega-terms vanish at s (their carriers are strict non-peaks, hence != l^±, so
their signatures vanish at s, and their targets miss s). For every block m', (R_{m'}^* w_{m'})(s) = [m' = m] lambda_{l^±}(±M_m) v_{l^±}(s) +
rest, where rest collects targets y_{l'} meeting s; such l' satisfy l' > l^± (allowedness (a)) and 2c_{l'} <= 2^{-2s} c_{l^±} delta_{l^±}
(allowedness (b)), so |rest| <= (4/3) sum_{l' >= L(s)} lambda_{l'} <= (2/9) 2^{-2s} c_{l^±} delta_{l^±} per block. Since
lambda_{l^±} v_{l^±}(s) >= (4/5) m 2^{-m-k(l^±)} c_{l^±} delta_{l^±} 2^{-s}, for s in S_{l^±} large (how large depending also on
max_{m'}|Delta d_{m'}|/|Delta d_m|, since v(s) = -sum_{m'} Delta d_{m'} (R_{m'}^* w_{m'})(s); see Proposition 5.6) the sign of v(s) is the sign of
-Delta d_m (±M_m) (if Delta d_m != 0). The sign condition at such s for l^+ and for l^- gives eps_0 Delta d_m <= 0 and eps_0 Delta d_m >= 0. QED.

**Proposition 5.2 ((H2') is automatic).** PROVED. By Lemma 5.0, each block has a swallowed peak of swallowing sign (w = eps_0 M) with
positive margin (l^up_m) and a swallowed peak of anti sign (l^dn_m); so (H2') of part 3 holds.

**Lemma 5.3 (signature lift).** PROVED for designs with c_l <= (delta_l ||h_l||_1)^2 for all l (an extra clause that can be added to (D1),
since ||h_l|| is fixed by (D0) before c_l is chosen; Proposition 2.4 is unaffected). There is l_0 (depending on f) such that every carrier
l >= l_0 with eps_0 y_l(zhat) >= 0 is a peak of swallowing sign with margin mu_l >= q_0 delta°_l/4.
*Proof.* For l large, S_l ∩ F = ∅ and sup_{S_l} |Ue| <= 1/4 (Ue in c_0), so eps_0 h_l(zhat) = ||h_l||_1 + eps_0 <h_l, Ue> >= (3/4)||h_l||_1.
Then eps_0 u_l(zhat) >= (3/4) delta°_l, while hat theta Phi_l <= hat theta c_l <= hat theta delta°_l^2 (5/4)^2 <= delta°_l/4 for l large. QED.
Hence M_f(l) <= 4 l Lambda°(l)/q_0 + M^canc_f(l), where M^canc_f(l) sums 1/mu over swallowing-sign peaks l' <= l with
eps_0 y_{l'}(zhat) < 0 (**signature-cancelling** carriers: the target value cancels most of the signature lift); likewise every strict
non-peak (|u_l(zhat)| < hat theta Phi_l) is signature-cancelling, and its gap is small only if |u_l(zhat)| is close to hat theta Phi_l.

**Corollary 5.4 (maximal contact).** PROVED (from Theorem 3.1, Prop. 5.2). For SLD_G, a maximal-contact first row f with F finite is in R
provided (H3) (no degenerate peak with w = eps_0 M), (DR), and
  liminf_l (1 + M^canc_f(l)/Lambda°(l))^2 / (gamma_f(l) (l 2^{l^3})^6) = 0.
(At maximal contact gamma_T = 1, and Lambda*_f(l) <= C_F Lambda°(l) because r*_l = 2 delta°_l, 1 + 3/(2 delta°_l) <= 1 + 2/delta°_l, for the
cofinitely many l with S_l ∩ F = ∅; so Xi_f(l) <= C (1 + M_f(l)/Lambda°(l))^2/gamma_f(l), and M_f/Lambda° <= 4l/q_0 + M^canc_f/Lambda°.)
For the original SLD the same holds with the factor H^Z_f(l)^4 Lambda°(l) of Corollary 4.1 and (l 2^{l^3})^6 replaced by l 2^{l^3}; there (DR)
is not needed.

**What is left of (O3).** Maximal contact first rows not covered by Corollary 5.4 / Corollary cor:BTrecovered must have one of:
 (a) a degenerate peak of swallowing sign (failure of (H3));
 (b) signature-cancelling swallowing-sign peaks whose margins decay so fast that M^canc_f(l)/Lambda°(l) is not o((l 2^{l^3})^3) along any
     subsequence (super-fast WEAK PEAKS), or strict non-peaks with gaps decaying faster than (l 2^{l^3})^{-6} (super-fast NEAR-THRESHOLD
     carriers) — both are (O1)(ii)-type objects;
 (c) failure of (DR) for SLD_G: some block has swallowed strict non-peaks with q_l != 0 but the zero-cost cone {tau >= 0 : sum tau_l u_l is
     eps_0-signed off F} contains no element with d-sum of one of the two signs (ONE-SIDED d-RESOURCES); for the original design: growth of
     the f-dependent Hoffman constants H^Z_f.
Note that for (b) the obstruction is not the number of swallowed carriers (B = L_N is handled) but the size of 1/margin and 1/gap; and for
(c) Proposition 5.1 shows that Corollary cor:D1's Delta d >= 0 cannot help.

**Remark 5.5 (scope of Corollary 5.4 beyond (BT)).** PROVED parts: (i) if M_f(l) <= (l 2^{l^3})^3 for all large l (so that (W_inf) is not
violated by M_f), then the margin-sparsity sum of (MS) restricted to swallowing-sign peaks is o(s): every margin of a swallowing-sign peak l is >= 1/M_f(l) >= nu_l := (l 2^{l^3})^{-3}, and
sum{Phi_k : mu_k < s} <= sum_{l >= l(s)} c_l <= (4/3) c_{l(s)}, l(s) := min{l : nu_l < s}, while c_{l(s)} <= T_lo(l(s)-1)^3 = o(nu_{l(s)}) = o(s)
(anti-sign peaks are not controlled by M_f, and Theorem 3.1 does not need them to be). (ii) Hence the maximal-contact first rows that
Corollary 5.4 adds to Corollary cor:BTrecovered are those violating (BT) through infinitely many strict non-peaks (with (DR) and gaps not
decaying faster than the ladder), or through weak or degenerate peaks of ANTI sign (failure of (MS) or degenerate peaks on the anti side). Failure of (MS) through
super-weak swallowing-sign peaks (margins comparable to Phi), and degenerate swallowing-sign peaks, are NOT covered: they are case (a)/(b)
of "what is left of (O3)". HEURISTIC: perturbing f to remove a super-weak peak (pushing u_l(zhat) below or above threshold) creates room or
near-contacts of the same tiny size elsewhere (on S_l or at a target coordinate), i.e. it converts (E-a) into (E-b), (E-c) or (E-e); no
perturbation of f removes the smallness.

**Proposition 5.6 (rigidity of the d-mismatch, general F finite).** PROVED. Let (b^±, omega^±) be two-piece data at f (F finite) with
Delta d_m := d_m(omega^-_m) - d_m(omega^+_m) != 0 for some block m. Put Delta := max_{m'} |Delta d_{m'}| and let T_omega be the finite union
of the target supports of the carriers in supp omega^±. For every peak carrier l of block m with S_l ∩ F = ∅, every s in S_l with
s > max T_omega and 2^{-s} < (2/5) |Delta d_m| M_m m 2^{-m-k(l)}/(N Delta) satisfies |z_s| = 1 and z_s = -sign(Delta d_m) sign(w_m(k(l))).
In particular Delta d_m = 0 as soon as block m has one peak carrier with infinitely many free points on its signature set, or infinitely
many contact points of each sign on one signature set, or two peak carriers of opposite signs whose signature sets carry infinitely many
contact points of the same sign (maximal contact: Proposition 5.1).
*Proof.* v := b^+ - b^- = sum_{m'} R_{m'}^*(delta omega_{m'} - Delta d_{m'} w_{m'}). At s as above the delta omega-terms vanish (s is outside
T_omega and outside the signature sets of the carriers in supp omega, which are strict non-peaks, hence different from l). For m' != m only
targets of carriers l' > l meet s (allowedness (a)), so |(R_{m'}^* w_{m'})(s)| <= (2/9) 2^{-2s} c_l delta_l (allowedness (b), as in the proof of
Proposition 5.1); for m' = m the same bound holds for (R_m^* w_m)(s) - lambda_l w_m(k(l)) v_l(s), and |lambda_l w_m(k(l)) v_l(s)| >=
(4/5) M_m m 2^{-m-k(l)} c_l delta_l 2^{-s}. Hence |v(s) + Delta d_m lambda_l w_m(k(l)) v_l(s)| <= N Delta (2/9) 2^{-2s} c_l delta_l <
|Delta d_m lambda_l w_m(k(l)) v_l(s)| by the choice of s, so sign v(s) = -sign(Delta d_m) sign w_m(k(l)) != 0. Two-piece data force v = 0 off
F ∪ K and z_j v(j) >= 0 on K; so s in K and z_s = sign v(s). QED.
Consequence: the option Delta d_m >= 0 of Corollary cor:D1 can only be used at first rows whose block-m peak signatures are all swallowed far out
with signs -sign(Delta d_m) sign(w(k(l))) ("peak-aligned swallowing"); outside that configuration two-piece data are d-neutral, and route (1)'s
"handle Delta d != 0 by Corollary cor:D1" has no room. (SC)/Theorem thm:engineered for Delta d < 0 is subject to the same rigidity, since it
concerns the same two-piece data.
