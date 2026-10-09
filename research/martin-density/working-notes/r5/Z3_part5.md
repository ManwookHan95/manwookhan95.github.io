# Z3 part 5 — (O1)(ii): weak peaks, near-threshold carriers, failure of (H3) and of (H2)

SLD operator unless stated; F finite; notation of Definition def:swallowed and Lemmas lem:modswallow-lem:windowtwopiece.

## 5.0 Observation (weak and near-threshold carriers matter only when B is infinite). PROVED.
If B is finite, Theorem thm:S (case B_fin) needs only (W*), (H2), (H3): weak bad peaks (alpha small but nonzero) enter only through the
finite constant max 1/(sigma|alpha(k(l))|) of Lemma lem:badpeaks(c), and near-threshold bad strict non-peaks only through
gamma_B = min of finitely many positive gaps (Lemma lem:windowtwopiece). So these items of (O1)(ii) are new only for infinitely many bad
carriers; for those, peaks are treated in 5.4 and non-d-neutral strict non-peaks remain open (5.6(a)). The gap condition is needed only
for OUTWARD block moves (Lemma 5.1): for the + side of the actual decomposition the outward part is <= (1 + O(t))gap/t automatically
(Lemma lem:suplevel(f)); gamma_B is used to absorb the outward part of the Hoffman correction (tau' - tau)/lambda_l <= 12/t.

## 5.1 Lemma (inward block moves need no gap). PROVED. (any admissible T)
Fix a block and drop its index. Let omega be finitely supported, k_0 in supp omega with alpha(k_0) = 0 (a degenerate peak or a strict
non-peak), and every other k in supp omega a strict non-peak. Put d := <Dw, D omega>/C, W(s) := (1 - ds)w + s omega, Y := C + dsM. Assume
|ds| <= 1/2, |ds|M <= C/2, |s omega(k)| <= gap(k)/2 for k in supp omega \ {k_0}, and at k_0 the move is INWARD and does not overshoot:
   sgn(w(k_0)) s omega(k_0) <= 0   and   |s omega(k_0)| <= (1 - ds)(M + |w(k_0)|)
(if w(k_0) = 0 the first condition is void and the second reads |s omega(k_0)| <= (1-ds)M). Then ||W(s)||_inf = (1 - ds)M,
<W(s) - w, zeta> = 0, and N(W(s)) <= 1 + (s^2/2) H(omega) (1 + 2|ds|M/C), H(omega) = (||D omega||^2 - d^2)/C.
*Proof.* Write D omega = (d/C) Dw + h_perp with h_perp ⊥ Dw; then D W(s) = (1 + dsM/C) Dw + s h_perp (1/C - 1 = M/C), so
||DW(s)|| = sqrt(Y^2 + s^2||h_perp||^2) <= Y + s^2||h_perp||^2/(2Y), and Y >= C/2. Off supp omega, |W(k)| = (1-ds)|w(k)|, with equality
(1-ds)M at the peaks with alpha != 0 (they exist, ||alpha||_1 = 1, and are not in supp omega). At k in supp omega \ {k_0}:
|W(k)| <= (1-ds)(M - gap(k)) + gap(k)/2 <= (1-ds)M. At k_0, with varsigma := sgn w(k_0): varsigma W(k_0) = (1-ds)|w(k_0)| - |s omega(k_0)|,
which lies in [-(1-ds)M, (1-ds)M] by the two conditions. Hence ||W(s)||_inf = (1-ds)M and N(W(s)) <= (1-ds)M + Y + s^2||h_perp||^2/(2Y)
= 1 + s^2 ||h_perp||^2/(2Y) <= 1 + (s^2/2)H(omega)(1 + 2|ds|M/C). Finally, by Lemma lem:threshold, <W(s) - w, zeta>/sigma =
s(<omega, alpha> + d - d(M + C)) = s omega(k_0) alpha(k_0) = 0. QED
*Meaning.* A degenerate peak, or a strict non-peak of arbitrarily small gap, is an exact ONE-SIDED block resource for inward moves, just as
a contact is an exact one-sided base resource. Lemma U (part 2) and Lemma lem:onesidedtransfer extend verbatim to pairs whose block parts
have, besides the coordinates allowed there, finitely many "inward coordinates" k with alpha(k) = 0, |omega(k)| <= A_2/t and the inward
sign for the side in question (varsigma_k omega(k) <= 0 on side +, >= 0 on side -): in the block step use Lemma 5.1 instead of Lemma
lem:block(d) (the no-overshoot condition holds for |r| <= c_flat t once c_flat A_2 <= M/4), and in the rebalancing step
||W_m - w_m||_inf <= 2A_3 c_flat still holds. PROVED (by inspection).

## 5.2 Identity (d-shift with bad peaks). PROVED.
Let B be finite, l_* >= max B, t in W(l_*), and (B_+-, Theta_+-) a two-sided decomposition. For a block m put
S_P := (M_m/C_m) sum_{l in B, m(l)=m, k(l) in P_m} Phi_m(k(l))^2 and, for bad peaks, e_l := varsigma_l eps_l tau_l/lambda_l - Delta d_m M_m
(>= 0 by (eq:peakshift); varsigma_l := sgn w_m(k(l))). Then
   Delta d_m M_m (1 + S_P) = - sum_{bad peaks in m} (Phi^2 M/C) e_l - sum_{bad strict non-peaks in m} q_l tau_l + r'_m,
   |r'_m| <= K_* t/(m C_m) + 2t/sigma_m.
*Proof.* (eq:didentity) and Lemma lem:modswallow(a) give Delta d M = - sum_{bad} q_l tau_l + r'. For a bad peak, q_l = eps_l Phi varsigma_l M/(mC)
and varsigma_l eps_l tau_l = lambda_l(Delta d M + e_l), so q_l tau_l = (Phi^2 M/C)(Delta d M + e_l) (lambda = m Phi). QED

## 5.3 Theorem S with weakened (H2) and (H3). PROVED (modifications of the proof of Theorem thm:S, case B_fin).
Let F be finite, B finite, (W*) hold, and for every block m one of:
 (A_m) m has a good non-degenerate peak [(H2) at m], and every bad degenerate peak k(l) of m with varsigma_l = eps_l lies in a block whose
       bad strict non-peak carriers all have q_{l'} >= 0 [(H3') at m];
 (B_m) m has no good non-degenerate peak, every bad strict non-peak carrier of m is d-neutral (q = 0) [(H2'') at m], and no bad
       degenerate peak of m has varsigma_l = eps_l [(H3) at m].
Then f in Rec.
*Proof.* Only Lemma lem:badpeaks (a), (c) and the peak part of the violation estimate in Lemma lem:exactswitch use (H2), (H3).
Case (A_m): (a) holds as stated. For a bad degenerate peak with varsigma = eps, 5.2 gives sum_{bad peaks}(Phi^2M/C)e_l = - sum_{np} q tau -
Delta d M(1+S_P) + r' <= sum_{np} q_l (tau_l)_- + C t <= C' t, because q_l >= 0 and (tau_l)_- <= c(tau)/(2 m_l) <= C t (proof of Lemma
lem:exactswitch); as all e_l >= 0, e_l <= C' t C/(Phi^2 M), and tau_l = lambda_l(Delta d M + e_l) = O(t). So |tau_l| = O(t) at every bad
peak, which is what Lemma lem:exactswitch and Lemma lem:windowtwopiece(b) use (rho_k <= |tau_l|/lambda_l + |Delta d|M).
Case (B_m): with q = 0 on bad non-peaks, 5.2 reads Delta d M(1 + S_P) + sum_P (Phi^2 M/C) e_l = r'. If Delta d >= 0 both terms are >= 0, so
|Delta d| M <= |r'|. If Delta d < 0: for non-degenerate bad peaks e_l <= t/(sigma|alpha(k)|); for degenerate bad peaks (varsigma = -eps by
(H3_m)) e_l = -tau_l/lambda_l - Delta d M <= (tau_l)_-/lambda_l + |Delta d|M; hence |Delta d|M(1 + S_P - (M/C) sum_{deg}Phi^2) <= C t, and
1 + S_P - (M/C)sum_{deg} Phi^2 >= 1. So (a) holds with a new K_d, and then (c) as in Lemma lem:badpeaks. The d-condition of the cone is
vacuous in such blocks (q = 0 on bad non-peaks, tau' = 0 at bad peaks). The rest of the proof of Theorem thm:S is unchanged. QED

## 5.4 Theorem S with infinitely many bad peaks (weak peaks). PROVED (modifications of the proof of Theorem thm:S, case B_res).
Let F be finite and B = B_np u B_pk, where B_np consists of resonant d-neutral (strict non-peak) carriers, B_pk of peak carriers, (H1)
holds for B, (H2) holds, (H3) holds (degenerate bad peaks have varsigma_l = -eps_l), and
 (W*_pk)  r*_l > 0 for good l, and liminf_l [Lambda*_f(l) + sum_{l' <= l, l' in B_pk, alpha(k(l')) != 0} 1/mu_{k(l')}] / (l 2^{l^3} Lambda°(l)) = 0.
Then f in Rec. (mu = margin, (eq:margin): sigma|alpha(k)| = lambda_k mu_k.)
*Proof.* Lemma lem:modswallow (a), (b) and the unified triangular system hold with B (the bad inequality only uses z = eps_l on S_l \ F and
(H1)). Lemma lem:badpeaks(a) holds by (H2) with K_d fixed. For l in B_pk non-degenerate: by (eq:peakshift) |tau_l| <= lambda_l(t/(sigma|alpha|)
+ |Delta d|M) = t/mu_{k(l)} + lambda_l K_d t; degenerate: tau_l <= lambda_l K_d t and (tau_l)_- <= K_* t (unified system). Keep tau' :=
(tau_l)_+ on B_np and tau' := 0 on B_pk (case (B_res) of Lemma lem:exactswitch): V' is z-signed in K by resonance, the d-condition is
vacuous, and ||Delta B 1_{F^c} - V'||_1 <= K_* t + sum_{B_np}(tau)_- + sum_{B_pk, l <= l_*}|tau_l| + 6t^2 <= K_pk t with
K_pk := C(K_* + sum_{l <= l_*, B_pk, nondeg} 1/mu_{k(l)} + K_d). Lemma lem:windowtwopiece goes through with K_pk in place of C_f K_* (at bad
coarse peaks omega^+ = 0 and rho_k <= |tau_l|/lambda_l + |Delta d|M; fine bad peaks are box-bounded, sum_{l>l_*}|tau_l| <= 6t^2; the bad
peaks' d-terms are not needed). The windows of (W*_pk) give K_pk T_hi(l_j) -> 0 and n^w_{l_j}/K_pk -> infinity, and the end of the proof of
Theorem thm:S applies. QED
*Remark.* The inverse margins enter ADDITIVELY (peak pinning is direct, not triangular), so weak bad peaks are harmless unless their
margins decay so fast that sum_{l <= L} 1/mu_l is not o(L 2^{L^3} Lambda°(L)) along any subsequence. B infinite with bad NON-peaks that
are not d-neutral remains outside (their d-condition couples infinitely many carriers; Hoffman constants are not controlled).

## 5.5 Failure of (H3) in general: tuning companions. SKETCH.
Let B be finite, (W*), (H2), and let k(l_0) be a bad degenerate peak with varsigma = eps_{l_0} in a block containing bad non-peaks with
q < 0 (so 5.3 does not apply). (i) [PROVED] At f the data of such a carrier are inward on BOTH sides (Lemma lem:suplevel(c)), so by 5.1 the
window data of Lemma lem:windowtwopiece with omega^+-(k(l_0)) := omega_+-(k(l_0)) satisfy the extended Lemma U; but Corollary cor:D1 needs
block parts in c_00(Q): at an engineered approximant the degenerate peak is unstable, and the theta-regime uses omega^theta(k(l_0)) for
both signs of tau (one of them outward). (ii) [SKETCH] Tuning companion: perturb f at a coordinate of a FINE good signature set S_{l'}
(l' > l_*, so no coarse target meets it by allowedness (a), and no window datum uses it) so that theta_m increases while u_{k(l_0)}(zhat) is
unchanged; then k(l_0) becomes a strict non-peak of tiny gap at a companion f^#_j whose cost can be made arbitrarily small AFTER the
window is chosen. At f^#_j the inward data are ordinary two-piece data (k in Q^#) and need no gap (5.1); the companion cone converges to
the cone of f with the row tau_{l_0} = 0 removed (bounded Hoffman constants). Theorem E then gives f in Rec. Missing step: the first-order
genericity statement "some coordinate of some fine good S_{l'} moves theta_m in the required direction" (it involves the clamp equation
of block m; generically true, not proved here).

## 5.6 What remains of (O1)(ii). OPEN.
 (a) B infinite with bad strict non-peaks that are NOT d-neutral (near-threshold carriers |w| close to M included): the exact d-neutral cone
     involves infinitely many carriers; same-sign weights q_l force the switching to be "d-pinned" only with constant ~ 1/lambda_l, which is
     not window compatible (K T_hi -> infinity). This is (O2)/(O3).
 (b) Blocks without a good non-degenerate peak and with non-d-neutral bad non-peak switching: 5.2 ties Delta d_m to the bad d-sum, both can
     be O(1); exact two-piece data then need Delta d_m != 0, which is impossible as soon as block m has a good carrier with w != 0
     (v = b^+ - b^- would contain -Delta d_m R_m^* w_m on a roomy signature set). Shifted (infinitely supported) two-piece data are needed.
 (c) Weak bad peaks with non-summable inverse margins in the sense of (W*_pk); (H3) failure without the tuning step of 5.5.
