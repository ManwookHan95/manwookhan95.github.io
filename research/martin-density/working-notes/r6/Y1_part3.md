# Y1 part 3 — Pinning at f on a clean sub-window (all rates robust or tiny)

Setting: D_X, N >= 1, f in S_{p*} with F finite, g in C(f), eta <= eta_* with eta_Gamma(eta) <= 1; w = (l,i) a CLEAN
sub-window (Theorem 2) with l >= l_f, where l_f (depending only on f) is >= max F and >= the indices of the finitely many fixed
carriers used below (donors, repair directions); t in W(w) dyadic, t <= min(t_eta, 1); (B_+-, Theta_+-) a two-sided
decomposition of g at scale t.  "f-constant" = number depending only on f, N (and g, rho where stated), not on l, w, t.
By Theorem 1(b) and (2.1): sum_{l' > l} |Delta theta_{l'}| <= 6 sum_{l'>l} lambda_{l'}/t <= 3 b(w)^2/t <= t^7, and b(w) <= t^4/l.

**Classification of the coarse carriers l'' <= l at w** (rate_1 = normalized room on S^nat_{l''}(l) = S_{l''} \ (F ∪ T(l))):
 * ROBUST-GOOD (class R): rate_1 >= u(w);
 * GENERALIZED-BAD (class G): rate_1 <= b(w).  Then eps_{l''} in {+-1} denotes a sign with
   r^nat_{l''}(l) = sum_{s in S^nat_{l''}} v_{l''}(s)(1 - eps_{l''} z_s), and tau_{l''} := -eps_{l''} Delta theta_{l''}.
   (Every exactly swallowed carrier of the note, z = eps on S_{l''} \ F, is in class G with r^nat = 0 and the same eps.)
For a G-carrier l'' = j(k,m): q_{l''} := eps_{l''} Phi_m(k) w_m(k)/(m C_m) (as in Definition def:swallowed); it is a
SWALLOWING-TYPE carrier if eps_{l''} sgn w_m(k) = +1 (then q > 0) and ANTI-TYPE if = -1 (q < 0); if w_m(k) = 0 it is d-neutral.
Relative positions rho (part 2): peak iff rho >= 1; near-threshold iff |rho - 1| <= b(w); NEARLY NEUTRAL iff rho <= b(w);
otherwise rho is robust on both counts (|rho - 1| >= u(w) and rho >= u(w)).  Put D := D(l) (Theorem 1), so lambda_{l''} >=
Phi_{l''} >= 1/D and m^nat_{l''}(l) >= 1/D for l'' <= l.

**Lemma 3.1 (diagonal pinning of class R).  PROVED.**  sum_{l'' in R} |Delta theta_{l''}| <= K_g t, K_g := (1/q_0 + 1) D/u(w).
Proof.  For s in S^nat_{l''}: no target of a coarse carrier contains s (s notin T(l)), coarser targets avoid S_{l''} (allowedness
(a)), other signatures vanish (disjointness); by (P1) and eq:DeltaB, -Delta B(s) = Delta theta_{l''} v_{l''}(s) + r(s),
r(s) := sum_{l' > l} Delta theta_{l'} y_{l'}(s)/n_{l'}.  By Lemma lem:phicalc(c),(d) (as in the proof of Lemma lem:signmixed),
r^nat_{l''} |Delta theta_{l''}| <= E_{l''} + 2 sum_{s in S^nat_{l''}} |r(s)|,  E_{l''} := sum_{s in S^nat_{l''}} phi_{z_s}(Delta B(s)).
The sets S^nat_{l''} are disjoint subsets of F^c, so sum E <= t/q_0 (Lemma lem:switchbudget), and sum_{l''} sum_s |r(s)| <=
(4/3) sum_{l'>l} |Delta theta_{l'}| <= 2t^7.  For l'' in R, r^nat_{l''} >= u(w) ||v_{l''} 1_{S^nat}||_1 >= u(w) m^nat_{l''}(l) >= u(w)/D.
QED  (No triangular unrolling, no product of rooms, no slaving: coarse targets are excluded from the pinning sets.)

**Lemma 3.2 (one-sided pinning of class G).  PROVED.**  sum_{l'' in G} (tau_{l''})_- <= K_g t, and
e_0 := Delta B 1_{F^c} - sum_{l'' in G} eps_{l''} tau_{l''} u_{l''} 1_{F^c} satisfies ||e_0||_1 <= K_g t + t^7.
Proof.  With the same r(s): Delta B(s) = eps tau v(s) - r(s) on S^nat_{l''}, and phi_{z_s}(eps tau v(s)) = |tau| v(s)(1 - eps z_s sgn tau)
>= (tau)_- v(s)(1 + eps z_s); by Lemma lem:phicalc(c), summing over S^nat_{l''},
(tau)_- sum v(s)(1 + eps z_s) = (tau)_-(2||v 1_{S^nat}||_1 - r^nat) <= E_{l''} + 2 sum|r(s)|,
and 2||v 1|| - r^nat >= ||v 1_{S^nat}|| >= 1/D because r^nat <= b(w)||v 1|| <= ||v 1||.  e_0 = -sum_{R ∪ fine} Delta theta u 1_{F^c},
||u||_1 <= 1, Lemma 3.1.  QED

**Lemma 3.3 (peak relations).  PROVED.**  Let k = k(l''), l'' <= l, be a peak of block m, vs := sgn w_m(k), mu its margin.
 (a) l'' in R: Delta d_m M_m <= |Delta theta_{l''}|/lambda_{l''}; if rho_{l''} >= 1 + u(w), also Delta d_m M_m >= -|Delta theta_{l''}|/lambda
     - t/(lambda mu), and 1/(lambda_{l''} mu_k) <= m D^2/(q_0 theta_m u(w)).
 (b) l'' in G anti-type: Delta d_m M_m <= (tau)_-/lambda and tau <= -lambda Delta d_m M_m.
 (c) l'' in G swallowing-type: tau >= lambda Delta d_m M_m, and if mu > 0: tau <= lambda(Delta d_m M_m + t/(lambda mu)).
Proof.  eq:peakshift: Y := |omega_+(k)| + |omega_-(k)| = -vs Delta Theta_m(k) - Delta d M >= 0, Y <= t/(sigma|alpha(k)|) = t/(lambda mu)
(eq:margin), and Delta Theta_m(k) = Delta theta/lambda = -eps tau/lambda.  (a) |vs Delta Theta| <= |Delta theta|/lambda.  The margin is
mu = q_0 Phi theta_m (rho - 1)/m >= q_0 Phi theta_m u/m (part 2), and lambda = m Phi >= Phi, Phi >= 1/D.  (b) vs eps = -1:
-tau/lambda - Delta d M = Y >= 0.  (c) vs eps = +1: tau/lambda - Delta d M = Y in [0, t/(lambda mu)].  QED

**Definition (shift sources at w).**  For a block m an UPPER source is: (U1) a peak of block m in class R; or (U2) an anti-type
G-peak; or (U3) every coarse G-carrier of block m with q < 0 is an anti-type peak or an anti-type strict non-peak with
|rho - 1| <= b(w) or rho <= b(w).  A LOWER source is: (L1) a class-R peak with rho >= 1 + u(w); or (L2) a swallowing-type G-peak
with rho >= 1 + u(w); or (L3) every coarse G-carrier of block m with q > 0 has rho <= b(w).  (SP_w): every block has an UPPER
and a LOWER source at w.  (This is (H2'') of the Z4 referee read at the window; with fixed exactly swallowed peaks it holds at
every window, e.g. at maximal contact by Lemma 5.0 of Z4: swallowing-type and anti-type peaks with margins >= q_0/4.)

**Lemma 3.4 (shift pinning).  PROVED.**  Under (SP_w): |Delta d_m| M_m <= K_d t for every m, K_d := C_f D^3/u(w), C_f an f-constant.
Proof.  Upper bounds: (U1), (U2) by Lemma 3.3(a),(b), Lemmas 3.1, 3.2 and lambda >= 1/D.  (U3): by eq:didentity,
 Delta d M = (1/(mC)) sum_{R ∪ fine} Phi w Delta theta - sum_{G, m(l'')=m} q tau + r_m,  |r_m| <= 2t/sigma_m
(for a G-carrier Phi w Delta theta/(mC) = -q tau).  The first sum is <= (K_g t + t^7)/(mC).  For q > 0: -q tau <= q (tau)_-,
summing to <= K_g t/C (|q| <= 1/C, |w| <= 1).  For q < 0, -q tau = |q| tau, and by (U3): at anti-type peaks tau <= -lambda Delta d M
(Lemma 3.3(b)); at anti-type strict non-peaks with |rho - 1| <= b, Lemma suplevel(f) gives vs(omega_- - omega_+)(k) >= -3 gap/t,
while vs(omega_- - omega_+)(k) = vs eps tau/lambda - Delta d |w(k)| = -tau/lambda - Delta d |w(k)|, so tau <= lambda(3gap/t - Delta d|w(k)|)
with gap = M(1 - rho) <= b; at carriers with rho <= b, |q| tau <= (b Phi M/(mC)) 6 lambda/t <= t^3.  Hence
 Delta d M (1 + sum_{anti-peaks, anti-np} |q| lambda) <= (K_g + 2)t/C_m + 2t/sigma_m + 3 sum|q| lambda b/t + N t^3,
and the bracket is >= 1.  Lower bounds symmetrically: (L1), (L2) by Lemma 3.3(a),(c) (with 1/(lambda mu) <= m D^2/(q_0 theta u));
(L3): every q > 0 term satisfies |q tau| <= t^3, and -q tau = |q| tau >= -|q|(tau)_- for q < 0.  QED

**Lemma 3.5 (carriers pinned at f).  PROVED.**  With K_P := K_g + K_d + C_f D^2/u(w):
 (a) anti-type G-peaks: |tau| <= K_P t;   (b) anti-type G strict non-peaks with |rho - 1| <= b(w): |tau| <= K_P t;
 (c) swallowing-type G-peaks with rho >= 1 + u(w): |tau| <= K_P t;    (d) class-R carriers: |Delta theta| <= K_g t.
Proof.  (tau)_- <= K_g t (Lemma 3.2) in (a)-(c).  (a) tau <= -lambda Delta d M <= K_d t.  (b) as in the proof of Lemma 3.4:
tau <= lambda(3b/t + K_d t) <= (3t^3 + K_d t).  (c) tau <= lambda K_d t + t/mu, 1/mu <= m D/(q_0 theta u) (Lemma 3.3(a)).  QED
(b) is new: a near-threshold strict non-peak of anti type is pinned like an anti-type peak; its tiny gap is NOT a rate that
needs exactification.  Its counterpart, a near-threshold carrier of swallowing type, is NOT pinned (tau_+ free).

**Lemma 3.6 (d-row pinning of one-signed blocks).  PROVED.**  Let Sigma_m(w) be the set of coarse G-carriers of block m that are
swallowing-type peaks, or strict non-peaks with rho > b(w) which are not anti-type near-threshold.  Call block m
SIGMA-ONE-SIGNED at w (sigma in {+-1}) if sgn q = sigma on Sigma_m(w).  Then for every l'' in Sigma_m(w):
 |tau_{l''}| <= K_O t,  K_O := C_f D^2 (K_g + K_P)/u(w).
Proof.  Z6 2.4 (re-derived by the Z6 referee, 1.4): in eq:didentity the terms of Sigma_m(w) are -q tau with q of one sign, so
sum_{Sigma_m} |q| (tau)_+ <= A_m := |Delta d|M + 2t/sigma + (1/(mC)) sum_{l notin Sigma_m} Phi|w||Delta theta_l| + sum_{Sigma_m} |q|(tau)_-.
Carriers outside Sigma_m(w): class R and fine (K_g t + t^7), anti-type peaks and anti near-threshold non-peaks (Lemma 3.5), G-carriers
with rho <= b (Phi|w||Delta theta| = Phi M rho |tau| <= b 6 lambda/t <= t^3).  So A_m <= C_f (K_g + K_P) t.  For l'' in Sigma_m(w):
|q| = Phi M/(mC) at peaks and |q| = Phi M rho/(mC) >= Phi M u(w)/(mC) at strict non-peaks (rho > b implies rho >= u at a clean
sub-window), and Phi >= 1/D.  QED

**Summary (kept/dropped at w).**  DROPPED (pinned at f with constants <= C_f D^3 K_g/u(w), i.e. design x u(w)^{-2}): class R;
anti-type G-peaks; anti-type near-threshold G strict non-peaks; swallowing-type G-peaks with robust margin; in sigma-one-signed
blocks the whole of Sigma_m(w).  KEPT (switching free, must be carried by exact data): the remaining G-carriers, namely
 (K1) swallowing-type strict non-peaks (q > 0), any gap;  (K2) anti-type strict non-peaks with rho <= 1 - u(w) (robust gap
 gap = M(1 - rho) >= M u(w));  (K3) nearly neutral strict non-peaks (rho <= b(w), incl. exactly d-neutral ones);
 (K4) near-threshold swallowing-type carriers (weak or degenerate peaks with rho in [1, 1+b], non-peaks with rho in [1-b, 1)),
 in blocks that are not one-signed.  In sigma-one-signed blocks only (K3) is kept.
