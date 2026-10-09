# Z3 notes (Round 5) — case (O1) of Remark rem:openZ: approximate swallowing and inexact free carriers

Setting: canonical base, finite block set I = {1..N} (p = p_N; Lemma lem:martintail transfers to Martin's p), the note
paper/martin_density_note.tex is the reference (numbering and notation). Parts 1-2 and Lemmas 3.1, 5.1 hold for every admissible T;
the rest is for the signature-ladder design T of Definition def:SLD (part 6 uses a harmless strengthening (D*) of the design).
Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN. Part files: Z3_part1..6.md (assembled below). Scripts: ctx/r5/Z3_work/.

## 0. Summary

**(a) "Approximately two-piece" Corollary cor:D1 — what is true.**
* At f itself NO first-order defect proportional to the scale is tolerable (Remark 1.5, PROVED as a statement about the bounds): data with
  defect D certify nothing below scale ~D, window data have D ~ t, and averaging AT f creates a kink of slope ~ T_hi/n. With fixed data,
  the engineered construction tolerates only defects below a positive threshold ~ T_0^2 (SKETCH). Wrong-signed contact mass that is NOT
  forced by the representation is already harmless (Lemma lem:split puts it into the l_1-small remainder); the genuine defect is
  switching through a carrier vector u_l whose signature set is only approximately swallowed.
* **The correct "approximate" version moves the first row (Theorem E, PROVED).** Exact two-piece data may live at a nearby first row
  f_j (same base support), built on a window of n_j dyadic scales, provided p*(f_j - f) = o((bottom of the window)^2) (scale decoupling)
  and the usual window conditions K_j T_j -> 0, n_j/K_j -> infinity hold; windowed averaging is done AT f_j (the mate g of f enters only
  through the zeroth-order error p*(f_j - f) at scales above the window), and Corollary cor:D1 is applied AT f_j.
* **Transplant (Proposition T, PROVED).** Window decompositions of g at f become exact d-neutral two-piece data at a coarse
  exactification f^# (contacts raised/flipped on the approximately swallowed coarse signature sets) with frozen error
  O((1 + C_H^#)(K_* + theta) t), provided: pinning at f off the exactified carriers, block stability c(delta) <= theta T_lo^2, and a
  Hoffman bound C_H^# for the companion cone. Two new identities drive it: raising/flipping converts the first-order defect of the
  switching EXACTLY into a d-mismatch at the companion (Lemma 1.2, Corollary 1.3), and the cost of a companion is governed by the
  UNWEIGHTED quantity sum_k min(lambda_k, |u_k(delta)|) (Lemma 3.1; numerically necessary, part 6).
* **Exactly which defects are tolerable:** those whose exactification cost c(delta) is o(T_lo^2) on windows where all other coarse carriers
  are pinned within the window budget and the companion cone is well conditioned. Two intrinsic limits (PROVED, as statements about
  the method): (i) the BAND — a carrier with room r_l, T_lo^2 << r_l << 1/K, can be neither pinned (needs n >~ 1/r_l) nor exactified
  (needs r_l << T_lo^2 = 4^{-n} T_hi^2); every design has band carriers for suitable f (rooms ~ 1/n(l)^2); (ii) a d-neutral carrier with
  positive room cannot be both exactly resonant and d-neutral at any companion with the same base part (Lemma 1.4): its companion cone
  is degenerate, Hoffman constant >~ 1/r_l (re-tuning the Hilbert part: SKETCH).

**(b) Application to (O1).**
* (O1)(i) near-contact tails / far sign changes: on FINITELY many signature sets always recovered (Proposition 4.1, by Theorems thm:Bpm,
  thm:S); the obstruction requires infinitely many carriers with super-geometrically decaying relative rooms. Then: recovered under
  "tower gaps" of the room sequence with good companion cones (Corollary 3.4, 4.3(i)); Lemma Z at such f reduces to lower
  semicontinuity along the far lowerings f^L in R_0^+- / R_S (Proposition 4.2) — i.e. (O1)(i) is a quantitative case of (O2); the band
  (4.3(ii)) is the precise remaining step (4.4). OPEN.
* (O1)(ii): weak bad peaks and near-threshold bad strict non-peaks matter only for infinitely many bad carriers (5.0, PROVED). Infinitely
  many bad PEAKS are recovered when inverse margins are window-summable (Theorem 5.4, PROVED: peak pinning is additive). Failure of (H2)
  is harmless when the bad strict non-peaks of the block are d-neutral, and failure of (H3) is harmless when the bad strict non-peaks of
  the block have weights q >= 0 (Theorem 5.3, PROVED, via the d-shift identity 5.2 and Lemma 5.1: inward block moves need no gap). The
  general (H3) case reduces to a tuning lemma (5.5, SKETCH). Remaining: infinitely many non-d-neutral bad strict non-peaks; (H2)-failing
  blocks with non-d-neutral switching (exact two-piece data impossible; shifted data needed) — OPEN (5.6).
* Structural: for the (slightly strengthened) SLD design, (BT) points are dense among finitely supported first rows (6.1, SKETCH:
  genericity step), so Lemma Z is a pure lower-semicontinuity statement along explicit approximants in G (6.2).
* No counterexample; nothing found points to one. Density remains OPEN.

| # | Statement | Status | Where |
|---|---|---|---|
| 1 | Effective contact set at scale t (budget on N_theta, wrong-signed mass O(t)) | PROVED | 1.1 |
| 2 | d-coefficients through the normer; defect identity at companions | PROVED | 1.2 |
| 3 | Raising/flipping converts the first-order defect into a d-mismatch (>= 0) | PROVED | 1.3 |
| 4 | Approximate resonance vs d-neutrality at companions (degenerate cones) | PROVED | 1.4 |
| 5 | No defect proportional to the scale is tolerable at f; kink of averaged defect data | PROVED (bounds) | 1.5(a,b) |
| 6 | Fixed data in Thm thm:engineered tolerate defects below ~ T_0^2 (s_1 may stay fixed) | SKETCH | 1.5(c) |
| 7 | Uniform one-sided transfer expansion along f_j -> f | PROVED | 2.1 |
| 8 | **Theorem E**: windowed recovery through nearby first rows (scale decoupling eps_j = o(T_lo^2)) | PROVED | 2.2 |
| 9 | Cost of a companion: l_1-change of block functionals <= C[Delta log(e/Delta) + sum min(lambda_k,|u_k(delta)|)] | PROVED (+num.) | 3.1, 6.3 |
| 10 | Budget of the actual decomposition at a companion | PROVED | 3.2 |
| 11 | **Proposition T**: transplant of window data to coarse exactifications | PROVED | 3.3 |
| 12 | Corollary: exactification windows => f in Rec | PROVED | 3.4 |
| 13 | (O1)(i) needs infinitely many carriers with super-geometric room decay | PROVED | 4.1 |
| 14 | (O1)(i) reduces to lsc along far lowerings (f^L in R_0^+- / R_S) | PROVED | 4.2 |
| 15 | Tower gaps suffice; band obstruction; d-neutral companion obstruction | PROVED (method) | 4.3 |
| 16 | Re-tuning the Hilbert part for d-neutral approximately resonant carriers | SKETCH | 4.3(iii) |
| 17 | Remaining (O1)(i): band carriers / lsc along far lowerings | OPEN | 4.4 |
| 18 | Weak/near-threshold carriers matter only for B infinite | PROVED | 5.0 |
| 19 | Inward block moves need no gap (one-sided block resources) | PROVED (+num.) | 5.1, 6.3 |
| 20 | d-shift identity with bad peaks | PROVED | 5.2 |
| 21 | Theorem S under (A_m) [(H2)+(H3')] or (B_m) [(H2'')+(H3)] per block | PROVED | 5.3 |
| 22 | Theorem S with infinitely many bad peaks, window-summable inverse margins | PROVED | 5.4 |
| 23 | (H3) failure via tuning companions | SKETCH | 5.5 |
| 24 | Infinitely many non-d-neutral bad non-peaks; (H2) failure with non-d-neutral switching | OPEN | 5.6 |
| 25 | Peak-ification: (BT) points dense among finitely supported first rows (design (D*)) | SKETCH | 6.1 |
| 26 | Lemma Z = lsc along explicit G-approximants | PROVED given 4.2 / 6.1 | 6.2 |

# Z3 part 1 — structural facts about first-order defects (any admissible T unless stated)

Notation of the note (paper/martin_density_note.tex). I finite, f in S_{p*} with forced data (xi, q_0, a, w, F, z, zhat, e, nu),
phi_z(x) := |x| - z x. A *companion* of f is a first row f^# with the SAME base part a and contact data z^# in B_{l_inf} with
z^# = z on F (= sgn a); it exists and is unique by Remark rem:lemmaZ(c) (data (a, z^#), e^# = e), and zhat^# = zhat + delta with
delta := z^# - z supported in F^c. Data of f^# carry the superscript #.

## 1.1 Lemma (scale-dependent effective contact set). PROVED.
Let (B_+-, Theta_+-) be a two-sided decomposition of g in C(f) at scale t > 0 (Lemma lem:twosided), F arbitrary. For theta in (0,1] put
N_theta := {j notin F : 1 - |z_j| <= theta} (contains K). Then
 (a) sum_{j notin F, j notin N_theta} |B_+-(j)| <= t/(2 theta q_0);
 (b) for theta < 1: sum_{j in N_theta} (sgn(z_j) B_+(j))_- <= t/(2(2-theta) q_0) and sum_{j in N_theta} (sgn(z_j) B_-(j))_+ <= t/(2(2-theta) q_0);
 (c) sum_{j in N_theta} (1 - |z_j|) |B_+-(j)| <= t/(2 q_0).
*Proof.* Lemma lem:switchbudget: sum_{j notin F} phi_{z_j}(B_+(j)) <= t/(2q_0), sum phi_{-z_j}(B_-(j)) <= t/(2q_0). Off N_theta,
phi_{+-z_j}(x) >= (1-|z_j|)|x| > theta|x|: (a). On N_theta (theta < 1, so z_j != 0), if sgn(z_j) x < 0 then phi_{z_j}(x) = (1+|z_j|)|x| >= (2-theta)|x|:
(b) (for B_- use phi_{-z_j}). (c): phi_{+-z_j}(x) >= (1-|z_j|)|x|. QED
*Meaning.* At scale t the switching can use, at bounded first-order cost, only coordinates of room <~ t/(mass): the effective contact set
K u N_theta shrinks to K as t -> 0. Approximate swallowing = switching on N_theta \ K with (1-|z|)-weighted mass O(t) (part (c)) but
l_1-mass not O(t) (Remark rem:budgetgloss). Wrong-signed mass on N_theta is always O(t) in l_1 (part (b)).

## 1.2 Lemma (d-coefficients through the normer; defect identity). PROVED.
(a) For every block m and omega in c_00(Q_m): d_m(omega) = (R_m^* omega)(zhat) / |R_m^** zhat|_m.
(b) If f^# is a companion and omega in c_00(Q_m cap Q^#_m), then
      |R_m^** zhat^#|_m d^#_m(omega) - |R_m^** zhat|_m d_m(omega) = (R_m^* omega)(delta).
*Proof.* (a) Lemma lem:threshold for zeta_m = R_m^** xi = q_0 R_m^** zhat: off P_m, Phi_m(k)^2 w_m(k)/C_m = zeta_m(k)/sigma_m. Hence
d_m(omega) = sum_k Phi_m(k)^2 w_m(k) omega(k)/C_m = <omega, zeta_m>/sigma_m = <omega, R_m^** zhat>/|R_m^** zhat|_m, and <omega, R_m^** theta> =
(R_m^* omega)(theta). (b) Apply (a) at f and at f^# and subtract; zhat^# - zhat = delta. QED

## 1.3 Corollary (raising converts a first-order defect into a d-mismatch). PROVED.
Let V := sum_l eps_l tau_l u_l (carriers k(l) in block m, strict non-peaks of f and of f^#), i.e. V = R_m^*(omega^- - omega^+) for the
switching omega^- - omega^+ := sum_l (eps_l tau_l / lambda_l) e_{k(l)}. If z^#_j in {+-1} and z^#_j V_j >= 0 for every j in supp delta, then
      |R_m^** zhat^#|_m Delta d^#_m - |R_m^** zhat|_m Delta d_m = V(delta) = sum_{j in supp delta} phi_{z_j}(V_j) >= 0,
where Delta d := d(omega^-) - d(omega^+). In words: if the switching is d-neutral at f, then at a companion which makes its near-contacts
(or wrong-signed contacts) exact contacts with the switching sign, it has d-mismatch EXACTLY equal to its first-order defect on the
modified coordinates divided by |R_m^** zhat^#|_m; in particular >= 0.
*Proof.* Lemma 1.2(b) with omega = omega^- - omega^+ and R_m^* e_{k} = lambda_{k,m} u_{k,m}. For j in supp delta, V_j delta_j = V_j(z^#_j - z_j) =
|V_j| - z_j V_j = phi_{z_j}(V_j) because z^#_j = sgn V_j when V_j != 0. QED
*Size.* For the projected window switching (Lemma lem:exactswitch, Lemma lem:split), V = Delta B 1_{F^c} up to l_1-error O(K t), so by
Lemma 1.1 and Lemma lem:phicalc(c) the right side is <= t/q_0 + O(K t): the d-mismatch created at a companion is O(K t)/sigma-scale.

## 1.4 Lemma (approximate resonance and d-neutrality are incompatible at companions). PROVED.
Let u in l_1, eps in {+-1}, and let f^# be a companion of f such that eps u_j z^#_j = |u_j| for all j in supp u \ F (eps u 1_{F^c} is
z^#-signed and supported in K^#). Then
      eps u(zhat^#) - eps u(zhat) = Re(u) := sum_{j notin F} phi_{z_j}(eps u_j) >= 0.
Consequently, if the carrier k = k(l) (u = u_l, eps = eps_l) is d-neutral at f (w_m(k) = 0, equivalently u(zhat) = 0) and its switching
direction has positive first-order defect Re(u_l) > 0 at f, then at EVERY companion at which it is exactly resonant and a strict
non-peak, w^#_m(k) = C^#_m m eps_l Re(u_l) / (Phi_m(k) |R_m^** zhat^#|_m) != 0: it is not d-neutral there, and its weight
q^#_l := eps_l Phi_m(k) w^#_m(k)/(m C^#_m) = Re(u_l)/|R_m^** zhat^#|_m > 0.
*Proof.* zhat^# - zhat = delta vanishes on F, and the U-parts coincide (same e). So eps u(zhat^#) - eps u(zhat) = sum_{F^c} eps u_j (z^#_j - z_j)
= sum_{F^c} (|u_j| - eps u_j z_j) = Re(u). For the second statement use Lemma lem:threshold at f^# (strict non-peak):
w^#_m(k) = C^#_m zeta^#_m(k)/(Phi^2 sigma^#_m) with zeta^#_m(k) = q^#_0 lambda_k u(zhat^#) and sigma^#_m = q^#_0 |R_m^** zhat^#|_m. QED
*Consequence for the method of Theorem thm:S at companions (PROVED).* If all switching carriers of a block are of this kind, every
q^#_l > 0 and the cone of exact d-neutral resonances at f^# (Lemma lem:exactswitch) meets {tau >= 0} only in 0: the Hoffman projection
at f^# then costs the whole switching, not O(K t). Exactness at a companion with the same base part therefore requires either
carriers of both signs of q^# in the block, or a re-tuning of the Hilbert part (moving a, hence e) — see part 4.

## 1.5 Remark (why fixed-defect data fail; the kink). PROVED (as a statement about the bounds), not a non-recovery claim.
(a) At f, a side-+ pair (b, omega) representing g with b(xi) = 0, omega in c_00(Q) and b supported in F u K u N gives, for 0 < r small,
p*(f + r g) <= 1 + q_0 r D^+(b) + (r^2/2)(Gamma_w(b,omega) + o(1)), D^+(b) := sum_{j notin F} phi_{z_j}(b_j)  (proof of Prop
prop:onesidedupper: the only change is Exc(r b) = r D^+(b) instead of 0, which enters the weighted excess Gamma-hat with weight q_0).
The term q_0 r D^+ is first order: such data certify NOTHING at scales r << q_0 D^+.
(b) At window scale t the defect of the projected window data is D^+ <= t/(2q_0) + O(K t) (Lemma 1.1), i.e. of the size of the whole
quadratic budget at scale t. Hence the one-sided transfer expansion (Lemma lem:onesidedtransfer: |r| <= c_flat t) fails for such data,
and in the windowed averaging at f (Theorem thm:windowed, Lemma lem:avgfunctionals) every coarse-scale piece t_i >> r contributes the
first-order term rho|r| q_0 D_i <= rho|r| t_i/2: the average carries a kink of slope ~ T_hi/n. This is the "exactness versus scale"
tension of Remark rem:openZ in quantitative form: no averaging AT f of defect data can produce a mate below scale ~ T_hi/n.
(c) In Theorem thm:engineered with FIXED data, a first-order defect enters Step 3 (base) as rho|tau| D (or, if the near-contacts are
raised in f', as a level shift rho|tau|E_v/2 removed by rebalancing at cost ~ iota |tau| E_v). Either way it is admissible only if it is
<= c delta s_1 with an admissible s_1 <~ T_0^2 (SKETCH: s_1 need not tend to 0; the construction with s_1 fixed and N_w, N'' -> infinity
converges to a companion-type first row, and all "o(s_1)" terms become s_1 * o_{s_1 -> 0}(1)). So fixed data tolerate only defects
below a positive threshold ~ T_0^2(data); window data have defect ~ T_hi/n >> T_0^2 ~ (n T_lo)^2. An "approximately two-piece Cor D1"
with defects proportional to the scale of the data is therefore NOT available at f; defects must be removed by changing the first row.
# Z3 part 2 — recovery through nearby first rows carrying exact window data (Theorem E)

Any admissible T, I finite. The point: the exact two-piece data needed by Corollary cor:D1 may live at a first row f_j close to f,
provided f_j is closer to f than the square of the BOTTOM of the window of scales on which the data are built.

## 2.1 Lemma U (uniform one-sided transfer expansion along a convergent sequence). PROVED (by inspection of the note's proofs).
Let f_j -> f in S_{p*}, with supp a_j = F finite for all j. For every eps_tr > 0, A_0, A_2 >= 1 and gamma_B in (0,1] there are
c_flat in (0, 1/8], t_1 > 0 and j_0 such that for every j >= j_0, every t in (0, t_1], and every side-+ (resp. side--) admissible pair
(b, omega) AT f_j with b(xi_j) = 0, t||b||_1 <= A_0, Gamma^{(j)}_w(b, omega) <= 2, and every k in supp omega_m satisfying either
[gap^{(j)}_m(k) >= t^2 and |omega_m(k)| <= 2 gap^{(j)}_m(k)/t] or [gap^{(j)}_m(k) >= gamma_B and |omega_m(k)| <= A_2/t], the functional
G := b + sum_m R_m^*(omega_m - d^{(j)}_m(omega_m) w_{j,m}) satisfies p*(f_j + rG) <= 1 + (r^2/2)(Gamma^{(j)}_w(b,omega) + eps_tr) for
0 < r <= c_flat t (resp. -c_flat t <= r < 0).
*Proof.* The proofs of Lemmas lem:uniformtransfer and lem:onesidedtransfer use f only through: |I|, ||U||, nu, a_min = min_F|a_i|,
q_0, sigma_m, C_m, M_m (via C_min, the bounds h(b) <= 2/q_0, H_m <= 2/sigma_m, e_{y,m} >= 1/2, and the radius conditions
c_flat <= min_m((M_m - gamma_m)/12, C_m/4)), and the transfer data (gamma_m, k^varsigma_{*,m}, Lambda^varsigma_m) of Lemma
lem:transferdata with the quantities iota, e_y, ||D_m y||, |Y|/q_0. All scalar data of f_j converge to those of f
(Proposition prop:continuity; a_{j,min} -> a_min > 0 because supp a_j = F and a_j -> a in l_1). Choose the transfer data AT f with
inefficiency eta_1 (as in the proof of Lemma lem:uniformtransfer); by Lemma lem:persistence they are transfer data of f_j for j large,
with iota_j <= 2 eta_1, e_{y,j} >= 1/2, ||D_m y_j||_2 <= K_y + 1, |Y_j|/q_0^{(j)} <= K_Y + 1. Every constraint on c_flat and t_1 in those
proofs is then satisfied uniformly for j >= j_0 if it is imposed with the limit constants and a factor 2 of room. The base step
(no flips on F, Psi-bound) and the block step (Lemma lem:block(d) at f_j with the coordinatewise radii given by the hypotheses on
supp omega) are pointwise in f_j and use only these constants. QED

## 2.2 Theorem E (windowed recovery through nearby first rows). PROVED.
Let T be admissible, I finite, f in S_{p*} with F finite, g in C(f), rho in (0,1), and eta_0 in (0,2] with rho^2(1+eta_0) <= (1+rho^2)/2.
Suppose there are first rows f_j -> f with supp a_j = F, constants A_0, A_2 >= 1, gamma_B in (0,1], and for every j numbers T_j in (0,1],
n_j in N, K_j >= 1 and, for every scale t in S_j := {T_j 2^{1-i} : 1 <= i <= n_j}, a functional g_{j,t} carrying d-neutral two-piece data
(b^+-, omega^+-) AT f_j (Definition def:twopiece read at f_j) with
 (E-a) b^+-(xi_j) = 0, t||b^+-||_1 <= A_0, Gamma^{(j)}_w(b^+-, omega^+-) <= 1 + eta_0/2;
 (E-b) the size conditions of Lemma U on supp omega^+-_m (with A_2, gamma_B);
 (E-c) p*(g - g_{j,t}) <= K_j t;
 (E-d) K_j T_j -> 0 and n_j / K_j -> infinity;
 (E-e) (scale decoupling) eps_j := p*(f_j - f) <= theta_j (T_j 2^{-n_j})^2 with theta_j -> 0.
Then (f, rho g) in cl NA((c_0,p), l_2^2). If the hypotheses hold for every rho < 1, then (f, g) in cl NA.

*Proof.* Let c_flat, t_1, j_0 be given by Lemma U for eps_tr := eta_0/2. Put t_i := T_j 2^{1-i}, n := n_j, K := K_j, tau_j := T_j 2^{-n},
gbar_j := (1/n) sum_i g_{j,t_i}, and fix r_0 in (0,1] with r_0^2 <= 1 - rho^2. Let j be so large that j >= j_0, T_j <= t_1,
n >= 48 rho^2 K/(c_flat(1-rho^2)), theta_j rho^2/c_flat^2 <= (1-rho^2)/24, eps_j <= (1-rho^2) r_0^2/6 and 2 rho K T_j/n <= (1-rho^2) r_0/6.
Two bounds for each i and real r:
 (A) if rho|r| <= c_flat t_i: p*(f_j + r rho g_{j,t_i}) <= 1 + (rho^2 r^2/2)(1 + eta_0)  (Lemma U, both sides, Gamma_w <= 1 + eta_0/2);
 (B') always: p*(f_j + r rho g_{j,t_i}) <= p*(f + r rho g) + eps_j + rho|r| K t_i <= s(rho r) + eps_j + rho|r| K t_i  (g in C(f), (E-c)).
By convexity p*(f_j + r rho gbar_j) <= (1/n) sum_i p*(f_j + r rho g_{j,t_i}).
Case |r| <= r_0. Let I_r := {i : c_flat t_i < rho|r|}; as the t_i are dyadic, sum_{I_r} t_i < 2 rho|r|/c_flat. If I_r = {} all terms obey
(A). Otherwise rho|r| > c_flat t_n >= c_flat tau_j, so by (E-e) eps_j <= theta_j tau_j^2 < theta_j rho^2 r^2/c_flat^2 <= (1-rho^2) r^2/24. Hence
 p*(f_j + r rho gbar_j) <= max{1 + (rho^2 r^2/2)(1+eta_0), s(rho r)} + eps_j + 2 rho^2 K r^2/(c_flat n)
                      <= max{1 + (rho^2 r^2/2)(1+eta_0), s(rho r)} + (1-rho^2) r^2/12 <= s(r),
exactly as in the proof of Theorem thm:windowed ((1+rho^2)/4 + (1-rho^2)/12 = (2+rho^2)/6, and 1 + r^2(2+rho^2)/6 <= 1 + r^2/2 - r^4/8
<= s(r) because r^2 <= 1 - rho^2; and s(rho r) + (1-rho^2)r^2/12 <= s(r) by Lemma lem:slack(a)).
Case |r| >= r_0. Using (B') for every i: p*(f_j + r rho gbar_j) <= s(rho r) + eps_j + 2 rho K T_j |r|/n <= s(rho r) + (1-rho^2) r_0 |r|/3 <= s(r),
since eps_j <= (1-rho^2) r_0^2/6 <= (1-rho^2) r_0|r|/6, and min(r^2,|r|) >= r_0|r|.
Hence rho gbar_j in C(f_j), and p*(rho gbar_j - rho g) <= (rho/n) sum_i K t_i <= 2 rho K T_j/n -> 0.
The averaged data Dbar_j := (1/n) sum_i (b^+-_i, omega^+-_i) are d-neutral two-piece data at f_j for gbar_j: the sign conditions on K_j,
the vanishing off F u K_j, finite supports in Q^{(j)}_m, the two representations (linear in the data, d^{(j)}_m linear) and
Delta d = 0 are preserved under averaging. By convexity of Gamma^{(j)}_w, kappa_w(Dbar_j) <= 1 + eta_0/2, so rho Dbar_j are d-neutral
two-piece data of rho gbar_j in C(f_j) with kappa_w <= rho^2(1 + eta_0/2) <= 1. Corollary cor:D1 at f_j (F finite, I finite) gives
(f_j, rho gbar_j) in cl NA. Finally ||(f_j, rho gbar_j) - (f, rho g)|| <= eps_j + 2 rho K_j T_j/n_j -> 0. QED

## 2.3 Remarks. 
(a) (PROVED) With f_j = f (eps_j = 0) Theorem E is exactly the mechanism of the proof of Theorem thm:S; (E-d) is what (W*) provides there.
(b) (PROVED) The only place where f_j != f costs anything is (B'): pieces of the window that are too fine for the scale r are compared
with the mate g of f, which is a mate of f_j only up to the zeroth-order error eps_j. Such pieces exist exactly for rho|r| > c_flat t_n,
hence (E-e). Below the window every piece obeys (A), so nothing else is needed there; above sqrt(eps_j) the slack does the work.
(c) (PROVED) Theorem E reduces Lemma Z (and recovery of the pair) to the TRANSPLANT problem: produce, from the two-sided decompositions of g
at f at the scales of a window, exact d-neutral two-piece data at a nearby first row f_j, with eps_j << (bottom of the window)^2.
(d) The approximants f_j are not required to lie in any recovered class; Corollary cor:D1 is applied at f_j itself (to a mate of f_j
built by averaging), so no lower semicontinuity of C along f_j -> f is needed.
# Z3 part 3 — transplanting window decompositions to exactifying companions (SLD operator)

T = operator of Definition def:SLD, N >= 1, I = {1..N}, p = p_N; f in S_{p*} with F finite, g in C(f).
A *coarse exactification* of f for a window index l_* is a companion f^# (part 1) with
   z^# := eps_l on S_l \ F for l in A,   z^# := z elsewhere,   delta := z^# - z,
where A is a finite set of coarse ladder indices (l <= l_*) such that z is NOT identically eps_l on S_l \ F (approximately swallowed
carriers; their rooms r_l at f may be positive). On supp delta, delta_j = eps_l - z_j: a *raise* if sgn z_j = eps_l (|delta_j| = 1-|z_j|),
a *flip* if z_j = -eps_l (|delta_j| = 2), otherwise a move of size <= 1 + |z_j|.

## 3.1 Lemma (cost of a companion). PROVED.
Put Delta_m := ||R_m^** delta||_1 = sum_k lambda_{k,m} |u_{k,m}(delta)| and
   c(delta) := sum_m [ Delta_m log(e/Delta_m) + sum_k min(lambda_{k,m}, |u_{k,m}(delta)|) ].
There are c_f, C_f (depending only on f, N, T) such that if max_m Delta_m <= c_f then
   |C^#_m - C_m| + |sigma^#_m - sigma_m| + |q^#_0 - q_0| <= C_f max_m Delta_m,
   sum_m ||R_m^*(w^#_m - w_m)||_1 <= C_f c(delta),   ||D_m(w^#_m - w_m)||_2^2 <= C_f c(delta)^2,
   p*(f^# - f) <= (1 + ||U||) C_f c(delta).
(A priori closeness: zeta^#_m = q^#_0 R_m^** zhat^# is l_1-close to (q^#_0/q_0) zeta_m when Delta is small, J_m is norm-to-weak*
continuous at zeta_m != 0 (smoothness of |.|_m) and D_m is weak*-to-norm continuous on bounded sets; so C^#_m -> C_m, M^#_m -> M_m as
max_m Delta_m -> 0, which is what "Delta below c_f" provides.)
*Proof.* Fix m, drop it; v_k := m|u_k(zhat)|/|R^**zhat|, v^#_k likewise. Clamp formula (proof of Lemma lem:F1): Phi_k w(k) =
sgn(u_k(zhat)) min(Phi_k M, C v_k), and C is the root in (0,1) of sum_k min(Phi_k(1-c)/c, v_k)^2 = 1. As |R^**zhat^#| - |R^**zhat|| <= Delta
and |u_k(zhat)| <= 1 + ||U||: |v^#_k - v_k| <= c_1(|u_k(delta)| + Delta) with c_1 depending on f. The proof of Lemma lem:F1 (strict decrease
of F(.; v) near C through a peak with alpha != 0; |min(x,s)^2 - min(x,s')^2| <= 2x|s - s'|) gives, once Delta is below a constant c_f
ensuring |C^# - C| <= r and |v^#_{k_nat} - v_{k_nat}| <= r, |C^# - C| <= c_2 sum_k Phi_k |v^#_k - v_k| <= c_3 Delta (sum_k Phi_k <= 1,
sum_k Phi_k |u_k(delta)| <= Delta/m). q_0 = (1 + sum_m |R_m^** zhat|)^{-1} and sigma_m = q_0|R_m^** zhat| move by O(Delta). For each k, as
in Lemma lem:F1, Phi_k|w^#(k) - w(k)| <= |C^#-C|(Phi_k + v_k) + C^#|v^#_k - v_k| (same signs or one vanishes) and <= C^#v^#_k + C v_k <=
c_4|u_k(delta)| (opposite signs: then both |u_k(zhat)|, |u_k(zhat^#)| <= |u_k(delta)|). With lambda_k = m Phi_k, |w|, |w^#| <= 1 and
min(a, x+y+z) <= x + min(a,y) + min(a,z):
   lambda_k|w^#(k) - w(k)| <= m|C^#-C| Phi_k + min(2 lambda_k, c_5 Delta) + min(2 lambda_k, c_5 |u_k(delta)|).
Sum over k: sum_k min(2 lambda_k, x) <= x(log_2(2m/x) + 3) for lambda_k <= m 2^{-m-k} (count the k with lambda_k > x/2, and sum the
geometric tail). This gives the l_1 bound. For the D-bound: ||D(w^# - w)||^2 <= max_k Phi_k|w^#(k) - w(k)| * sum_k Phi_k|w^#(k)-w(k)|;
the second factor is (1/m) sum_k lambda_k |w^#(k) - w(k)| <= C c(delta), and by the two pointwise bounds above together with
Phi_k|w^#(k) - w(k)| <= 2 Phi_k, the first factor is <= c_6 Delta + min(2 Phi_k, c_6 |u_k(delta)|) <= c_7 c(delta) (each term of c(delta)
dominates the corresponding quantity). Finally f^# - f = L^*(w^# - w) and p* <= q* <= (1+||U||)||.||_1 on X*. QED

## 3.2 Lemma (budget of the actual decomposition at the companion). PROVED.
Let (B_+-, Theta_+-) be a two-sided decomposition of g at f at scale t. Then
   sum_{j notin F} phi_{z^#_j}(B_+(j)) <= t/q_0 + 2 sum_{j flipped} |B_+(j)|,
and the same for phi_{-z^#_j}(B_-(j)). On raised coordinates phi_{z^#_j}(x) <= 2 phi_{z_j}(x); on flipped ones phi_{z^#_j}(x) <= 2|x|.
*Proof.* Raised j (z^#_j = sgn z_j, |z_j| < 1): if sgn x = sgn z_j, phi_{z^#}(x) = 0; otherwise phi_{z^#}(x) = 2|x| <= 2(1+|z_j|)|x|/(1+|z_j|)
= 2 phi_{z_j}(x)/(1+|z_j|). Flipped: phi_{-z}(x) = |x| + zx <= 2|x|. Elsewhere phi_{z^#} = phi_z. Lemma lem:switchbudget. QED

## 3.3 Proposition T (transplant). PROVED (by the indicated modifications of Lemmas lem:modswallow-lem:windowtwopiece).
Let l_* be a window index and f^# a coarse exactification of f with set A. Let B be the set of exactly swallowed carriers of f, assume
B is finite with max B <= l_*, and put B' := A u B. Assume, with constants independent of the scale t in W(l_*):
 (P) [pinning at f] r*_l > 0 for good l notin B', where r*_l is computed at f with B' in place of B (Definition def:swallowed), (H1) for
     B' (targets of l' in B' do not meet S_l for l < l', l, l' in B'), and at f the conditions (H2) and (H3) hold for B'
     (the swallowing signs of l in A are the eps_l above). Put K_* := (1/q_0 + 22) Lambda*_{f,B'}(l_*).
 (BS) [block stability] Delta := max_m Delta_m <= c_f and c(delta) + Delta <= theta T_lo(l_*)^2 for a theta <= 1; every coarse k
     (j(k,m) <= l_*) has the same status at f and f^# (peak with the same sign / strict non-peak), and every k(l), l in B', that is a
     strict non-peak at f has gap^#(k(l)) >= gamma_B > 0.
 (HF) [Hoffman] the polyhedron Z^# defined at f^# by the conditions of Lemma lem:exactswitch for B' (tau_l >= 0; z^#-signs on T_0 cap K^#;
     vanishing on T_0 \ (F u K^#); tau_l = 0 at peaks; sum_{m(l)=m} q^#_l tau_l = 0 for every m), together with the box rows
     tau_l <= 6 lambda_l/t, has Hoffman constant <= C_H^# (Hoffman constants do not depend on the right sides).
Then for every t in W(l_*) with t <= min(t_eta, 1) and (C_H^# + 1) K_* t <= 1, g has a functional g_t carrying d-neutral two-piece data
AT f^# satisfying (E-a), (E-b) of Theorem E with A_0, A_2 = 10 and gamma_B independent of t, and
     p*(g - g_t) <= C (1 + C_H^#)(K_* + theta) t ,   Gamma^#_w(b^+-, omega^+-) <= (sqrt(1+eta_Gamma(eta)) + C(1 + C_H^#)(K_* + theta) t)^2,
where C depends only on f, N, gamma_B and the design.
*Proof (the changes w.r.t. the proofs of Lemmas lem:modswallow, lem:badpeaks, lem:exactswitch, lem:windowtwopiece).*
(1) Pinning at f modulo B'. The proof of Lemma lem:modswallow uses only that the right sides of the good inequalities contain good later
indices; with B' in place of B it gives sum_{l notin B'} |Delta theta_l| <= K_* t and, for l in B', the bad inequality
(tau_l)_- <= (E_l + ...)/r*_l with r*_l >= (2 - max(1-|z|))||v_l 1_{S_l \ F}||-type constant (on S_l \ F, phi_{z_s}(-Delta theta_l v_l(s))
>= (1 + eps_l z_s)(tau_l)_- v_l(s) and 1 + eps_l z_s is bounded below on the part of S_l \ F where z is close to eps_l, which carries all but
the room of the v_l-mass). Lemma lem:badpeaks holds verbatim at f for B' ((H2), (H3) for B').
(2) Violations at f^#. With L(tau) := sum_{l in B'} eps_l tau_l u_l and the actual amplitudes tau, ||Delta B 1_{F^c} - L(tau)1_{F^c}||_1 <=
K_* t + 6t^2. Cost at f^#: by Lemma 3.2 and Lemma lem:phicalc(c), c^#(tau) := sum_{j notin F} phi_{z^#_j}(L_j(tau)) <= 2t/q_0 + 2 S_fl + C K_* t,
S_fl := sum_{flipped j} |Delta B(j)|; on a flipped j in S_l, Delta B(j) = eps_l tau_l v_l(j) + O(pinned), and phi_{z_j}(eps_l tau_l v_l(j)) =
2(tau_l)_+ v_l(j) is part of the budget at f, while (tau_l)_- is bounded by (1); so S_fl <= C K_* t. Peaks: as in Lemma lem:exactswitch,
|tau_l| <= C lambda_l t at non-degenerate bad peaks and tau_l <= lambda_l K_d t at degenerate bad peaks of sign -eps_l ((BS): same peaks at
f^#). d-conditions at f^#: by Lemma 1.2(b) and 1.3, for every m,
   |R_m^** zhat^#| sum_{m(l)=m, k(l) in Q} q^#_l tau_l - |R_m^** zhat| sum_{m(l)=m, k(l) in Q} q_l tau_l = V_m(delta),
V_m := sum_{m(l)=m, k(l) in Q} eps_l tau_l u_l; by (H1) for B' the signature coordinates of supp delta carry only their own carrier, so
|V_m(delta)| <= sum_{raised} (1-|z_j|)|V_m(j)| + 2 sum_{flipped}|V_m(j)| + C K_* t <= C(t + K_* t) (Lemma 1.1(c) and the bound on S_fl), while
|sum q_l tau_l| <= C K_* t by Lemma lem:badpeaks(b) at f. The box rows hold exactly (Lemma lem:box). Hence the total violation of the
rows of (HF) by tau is <= C K_* t.
(3) Projection. Hoffman gives tau' in Z^# with tau'_l <= 6 lambda_l/t and sum |tau_l - tau'_l| <= C C_H^# K_* t; V' := L(tau')1_{F^c} is
z^#-signed and supported in K^#, and ||Delta B 1_{F^c} - V'||_1 <= C(1 + C_H^#) K_* t.
(4) Split and data. Lemma lem:split holds with z^# in place of z, its proof using only phi_{z^#_j}(B_+(j)) + phi_{-z^#_j}(B_-(j)) summed
(Lemma 3.2: <= 2t/q_0 + C K_* t) and V' z^#-signed in K^#: B_+ 1_{F^c} = chi V' + e_+, B_- 1_{F^c} = -(1-chi)V' + e_- with ||e_+-||_1 <=
C(1 + C_H^#)K_* t. Define the data exactly as in Lemma lem:windowtwopiece but AT f^#: omega^+_m := clamp of omega_{+,m} at the coarse
strict non-peaks with the gaps of f^# (Definition def:windowcert with gap^#), and omega^+_m(k(l)) := omega_{+,m}(k(l)) at the switching
non-peaks; omega^- := omega^+ + sum (eps_l tau'_l/lambda_l) e_{k(l)}; b^+ := B_+ 1_F + chi V' - kappa^# a with kappa^# := (B_+1_F + chi V')(zhat^#);
b^- := b^+ - sum eps_l tau'_l u_l; g_t := b^+ + sum_m R_m^*(omega^+_m - d^#_m(omega^+_m) w^#_m). Two-piece admissibility at f^#, the second
representation and Delta d^# = sum q^#_l tau'_l = 0 are verified as in Lemma lem:windowtwopiece(a).
(5) Estimates. kappa^# = B_+(zhat^#) - (e_+)(zhat^#) - ... and B_+(zhat^#) = B_+(zhat) + B_+(delta), |B_+(zhat)| <= t/(2q_0), |B_+(delta)| <=
sum_{raised}(1-|z_j|)|B_+(j)| + 2 sum_{flipped}|B_+(j)| <= C K_* t; hence |kappa^#| <= C(1+C_H^#)K_* t. The comparison of g_t with
g = B_+ + sum R_m^* Theta_{+,m} is that of Lemma lem:windowtwopiece(b) plus the terms coming from replacing (d, w, gap) by (d^#, w^#, gap^#):
 * sum_m R_m^*(d^#_m(omega^+)w^#_m - d_m(omega^+)w_m) = sum d^#(w^# - w)-terms + (d^# - d)w-terms; |d^#_m(omega^+)| <= 4/t ((d) of Lemma
   lem:windowtwopiece), ||R^*(w^# - w)||_1 <= C_f c(delta) <= C theta t^2 (Lemma 3.1, (BS)); by Lemma 1.2(b), |d^# - d|(omega^+) <=
   (|(R^*omega^+)(delta)| + |d(omega^+)| Delta)/|R^** zhat^#| with |(R^*omega^+)(delta)| <= ||omega^+||_inf Delta <= (10/t) theta t^2;
 * re-clamping with gap^# instead of gap changes omega^+ by at most 2|gap^#(k) - gap(k)|/t <= 2(|w^#(k) - w(k)| + |M^# - M|)/t at coarse
   k, whose lambda-weighted sum is <= C theta t;
 * status is unchanged at coarse k by (BS).
So p*(g - g_t) <= (1+||U||)||g - g_t||_1 <= C(1+C_H^#)(K_* + theta)t. For Gamma^#_w: sqrt(Gamma^#_w) is a seminorm; compare the + data with
(B_+, Theta_+) and the - data with (B_-, Theta_-) as in Lemma lem:windowtwopiece(c), and use Gamma^#_w(B_+-, Theta_+-) <=
Gamma_w(B_+-, Theta_+-) + C(||D(w^# - w)|| + |C^# - C| + |q^#_0 - q_0| + |sigma^# - sigma|)(1 + ||D Theta_+-||)^2 with ||D Theta_+-|| <= 4/t
(box) and ||D(w^#-w)|| + Delta <= C sqrt(theta) t (Lemma 3.1, (BS)): the P^perp-projections onto (D w^#)^perp and (D w)^perp differ in
operator norm by <= 2||D(w^# - w)||/C + 2|C^# - C|/C. Size conditions (E-b): coarse coordinates as in Lemma lem:windowtwopiece(d) with
gap^#; switching coordinates: |omega^+(k(l))| <= 4/t and |omega^-(k(l))| <= 4/t + tau'_l/lambda_l <= 10/t (box rows), gap^# >= gamma_B by (BS).
t||b^+-||_1 <= A_0 as in Lemma lem:windowtwopiece(d). QED

## 3.4 Corollary (exactification windows). PROVED (Theorem E + Proposition T).
If there are window indices l_1 < l_2 < ... and coarse exactifications f^#_j for W(l_j) satisfying (P), (BS) with theta_j -> 0
(T_lo := T_lo(l_j), the bottom of the design window, whose n^w_{l_j} dyadic scales are all used), and (HF) with
   (1 + C^#_{H,j}) K_{*,j} T_hi(l_j) -> 0  and  n^w_{l_j} / ((1 + C^#_{H,j}) K_{*,j}) -> infinity,
with gamma_B uniform, then f in Rec. (Here (E-e) follows from (BS) and Lemma 3.1: p*(f^#_j - f) <= C c(delta_j) <= C theta_j T_lo(l_j)^2;
in (E-c), K_j := C(1 + C^#_{H,j})(K_{*,j} + 1).) In particular every first row with F finite in which the approximately swallowed
carriers can be exactified window by window at cost c(delta_j) = o(T_lo(l_j)^2), with good companion cones and with the remaining
coarse carriers pinned within the window budget, is recoverable.
# Z3 part 4 — consequences for (O1)(i): approximate swallowing

SLD operator, N >= 1, F finite throughout. Rooms r_l (sign-mixed rooms of Theorem thm:Bpm), r*_l (Definition def:swallowed).

## 4.1 Proposition ((O1)(i) is an infinitely-many-carriers phenomenon). PROVED.
(a) If F is finite, every r_l > 0, and r_l >= varpi^l delta°_l for all but finitely many l (some varpi in (0,1]), then f in R_0^+- subset Rec.
(b) If B is finite and f satisfies (H2), (H3), and r*_l >= varpi^l delta°_l for all but finitely many good l, then f in R_S subset Rec.
In particular near-contact tails or far sign changes on FINITELY many signature sets never obstruct recovery, however fast |z_j| -> 1
there: the obstruction (O1)(i) requires infinitely many carriers whose relative rooms r_l/delta°_l decay faster than any geometric
sequence along every subsequence (failure of (W+-), resp. (W*)).
*Proof.* (a) For the finitely many exceptional l the factors 1 + 3/r_l contribute a constant C_0 to Lambda^+-_f(l); for the others
1 + 3/r_l <= (3/(2 varpi^l))(1 + 2/delta°_l) as in the proof of Theorem thm:Bpm. Hence Lambda^+-_f(l) <= C_0 (3/2)^l varpi^{-l^2} Lambda°(l)
and (W+-) holds; Theorem thm:Bpm. (b) Same computation for Lambda*_f (bad factors are 1 + 3/(2||v_l 1_{S_l\F}||) <= 1 + 2/delta°_l
up to a constant, and only finitely many l are bad); (W*) holds; Theorem thm:S (case B_fin). QED

## 4.2 Proposition (reduction of (O1)(i) to lower semicontinuity along far lowerings). PROVED.
Let F be finite, B finite, and let f satisfy (H2), (H3) (vacuous if B is empty). For L so large that S_l cap F = {} and l notin B for
l > L, let f^L be the far lowering of Remark rem:openZ(O2) (z^L := 0 on union_{l>L} S_l). Then f^L in R_S (in R_0^+- if B is empty), and
f^L -> f. Consequently, at every (O1)(i) point of this kind, Lemma Z holds for (f, g, rho) as soon as dist(rho g, C(f^L)) -> 0 along
some L -> infinity: (O1)(i) is contained in the lower-semicontinuity question (O2).
*Proof.* f^L has base part a and z^L = sgn a on F, so it is a companion of f; z^L -> z coordinatewise, so f^L -> f (Remark rem:openZ(O2)).
At f^L the room of S_l, l <= L, is that of f (the S_l are disjoint and z^L = z on S_l), and for l > L it is ||v_l 1_{S_l}||_1 = delta°_l
(S_l cap F = {}, z^L = 0 there). Hence only the finitely many rooms with l <= L can be small, and the bad set of f^L is B. If B = {}, all
rooms of f^L are positive and 4.1(a) gives f^L in R_0^+-. If B != {}: (H2) at f^L for L large — a good non-degenerate peak k°_m of f has
positive margin, which persists along f^L -> f (Proposition prop:continuity and Lemma lem:threshold), and its carrier stays good (its room
is unchanged); (H3) at f^L for L large — a bad carrier k(l) of f is either a strict non-peak with positive gap (persists), or a
non-degenerate peak (persists, with the same sign), or a degenerate peak with sgn w_m(k(l)) = -eps_l by (H3) at f; since w^L_m(k(l)) ->
w_m(k(l)) != 0, if it is a degenerate peak of f^L its sign is still -eps_l. So (W*) holds at f^L by 4.1(b) and f^L in R_S. QED

## 4.3 The companion route and its exact limits. PROVED (as statements about the method of parts 2-3).
Corollary 3.4 recovers f when, for infinitely many windows W(l_j), the coarse carriers split into
  pinned:      r*_l large enough that Lambda* (product over pinned coarse l) satisfies K_* T_hi -> 0, n^w/K_* -> infinity;
  exactified:  c(delta_j) <= theta_j T_lo(l_j)^2, theta_j -> 0, with well-conditioned companion cones (HF).
For a carrier exactified by raising (case (a)) or flipping (case (b)) on S_l, Lemma 3.1 gives c(delta) >= min(lambda_l, |u_l(delta)|) >=
min(lambda_l, r_l) up to constants (|u_l(delta)| = removed room of S_l, Lemma 1.4). Hence:
 (i) [Room gaps suffice] If there are infinitely many j such that every coarse l <= l_j has either r*_l >= rho_j or r_l <= theta_j
     T_lo(l_j)^2 (with lambda_l-weighted targets ignored), with prod_{l <= l_j, r*_l >= rho_j} (1 + 3/r*_l) = o(l_j 2^{l_j^3} Lambda°(l_j)),
     and the companion cones are well conditioned, then f in Rec. This needs "tower gaps": r_{next} <= exp(-C prod(1/r)) infinitely often.
 (ii) [The band] If, for all large windows, some coarse carrier has room in the band
          theta T_lo(l_*)^2 << r_l << 1/K_*(l_*),
     the method fails at that window: pinning needs n^w >~ 1/r_l, exactification needs r_l << T_lo^2 = 4^{-n^w} T_hi^2. Example: r_l =
     2^{-l^4} delta°_l for infinitely many l in one block: every window W(l_*) contains band carriers (2^{-l^4} >> 4^{-n^w_{l_*}} for l <= l_*,
     and prod_{l<=l_*} 2^{l^4} >> 2^{l_*^3}). The band is intrinsic to window methods: with any design whose windows have length n(l),
     pinning costs n >~ 1/r and exactification needs r << 4^{-n}; rooms r_l ~ 1/n(l)^2 lie in the band of every window. So no choice of
     design removes it (cf. Remark rem:nodesign for the first-order version).
 (iii) [d-neutral carriers] If the exactified carriers of a block are d-neutral at f and carry positive defect, every companion with the
     same base part has q^#_l > 0 for all of them (Lemma 1.4), so its cone forces tau' = 0 in that block and C^#_H >= c/min r_l: the
     companion buys nothing over pinning. Re-tuning the Hilbert part (moving a, possibly with tiny masses on contacts unused by the data, so
     that u_l(zhat^#) = 0 again) removes this obstruction for finitely many carriers per window at cost ~ ||Gram^{-1}|| max r_l
     (SKETCH: the masses must avoid the supports of the window data so that a_min plays no role in Lemma U).

## 4.4 What remains of (O1)(i) (precise statement). OPEN.
After 4.1 and 4.2, (O1)(i) is the following special case of (O2): F finite, infinitely many carriers with positive rooms r_l (or r*_l)
whose relative rooms decay super-geometrically (failure of (W+-)/(W*)) with no tower gaps; the mate g switches through infinitely many
of them at scales t in [sqrt(lambda_l r_l), C lambda_l] (the "free regime" of carrier l: |Delta theta_l| <= min(t/(q_0 r_l), 6 lambda_l/t)).
Remaining step: a recovery mechanism for switching through a carrier in its free regime that tolerates its first-order defect
tau_l r_l <= 6 lambda_l r_l/t, i.e. either (A) lower semicontinuity dist(rho g, C(f^L)) -> 0 along far lowerings (4.2), or (B) a variant of
windowed averaging in which a carrier's frozen error enters through log(1/r_l) instead of 1/r_l (the obstruction in (ii) is the single
scale t ~ sqrt(lambda_l r_l), where the pieces carry switching ~ sqrt(lambda_l/r_l) = t/r_l; an averaging scheme that excludes these
scales must still cover them at the coarser scales, where their frozen error enters through (B')).
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
# Z3 part 6 — density of block-tame first rows; Lemma Z as pure lower semicontinuity; numerics

## 6.1 Proposition (peak-ification: (BT) points are dense among finitely supported first rows). SKETCH (all steps written except
the final genericity step, see the caveat; status changes of the finitely many coarse carriers are harmless for (BT), only EXACT
degeneracy at f_L must be avoided, i.e. theta^L_m must avoid the finitely many values |u_l(zhat)|/Phi_l, l < L, m(l) = m; theta^L_m is a
continuous, non-constant function of the first push x_L on each interval where the recursion has no case switch, because
d|zeta|_m = sum_k w_m(k) d zeta_m(k) and k(L) is a peak with |w| = M, while the induced changes of the later pushes have total weight
sum_{l>L} lambda_l/delta°_L << lambda_L).  Statement under (D*):
Let T be the SLD operator, and assume the design satisfies
 (D*)  c_l psi_l <= delta°_l / 8 for all large l, for some psi_l -> infinity
(this can be arranged without affecting Theorem thm:SLD: choose the sets S_l recursively, S_l after c_l is known, with
min S_l <= (1/4) log_2(1/c_l), disjoint from all previously used coordinates and target supports; then delta°_l >~ min(2^{-l} c_l^{1/4}, 1)).
Let f in S_{p*} have F finite and no degenerate peaks. Then there are first rows f_L -> f (L -> infinity) with the same base part a,
each satisfying (BT); in particular f_L in R_BT subset Rec (Corollary cor:BTrecovered).
*Proof.* Fix L so large that no S_l, l >= L, meets F. Recursively in l >= L define delta on S_l \ F (and delta := 0 elsewhere):
let V_l := u_l(zhat + delta_{<l}), where delta_{<l} is the part already defined; only the target y_l can see delta_{<l}, and v_l does not.
Put A_l := 3 theta_{m(l)} Phi_l + psi_l Phi_l with Phi_l := Phi_{m(l)}(k(l)), theta_m the threshold constant of f. Choose a push sign
sigma_l for which the coordinates s in S_l \ F with sigma_l z_s < 1 carry v_l-mass >= ||v_l 1_{S_l\F}||/2 (one of the two signs does), and
put delta_s := sigma_l kappa_l on those coordinates with kappa_l in [0, 1] chosen so that x_l := v_l(delta 1_{S_l}) satisfies
|V_l + x_l| >= A_l with |x_l| <= 2 A_l (if sgn V_l = sigma_l or V_l = 0 take |x_l| = A_l, otherwise |x_l| = |V_l| + A_l <= 2A_l).
This is possible since 2A_l <= delta°_l/4 for l large by (D*) (Phi_l <= c_l). Moves keep |z_s + delta_s| <= 1 (sigma_l z_s < 1 and
kappa_l <= 1 - ... after shrinking kappa on coordinates close to sigma_l; the available mass bound absorbs this).
For l' > l, u_l(delta 1_{S_{l'}}) = 0 (y_l avoids S_{l'} by allowedness (a), v_l lives on S_l), so at the final point
|u_l(zhat + delta)| = |V_l + x_l| >= A_l. Cost: |u_l(delta)| <= 2A_l + |y_l(delta_{<l})| and lambda_l <= c_l, so by Lemma 3.1
p*(f_L - f) <= C c(delta) <= C sum_{l >= L} lambda_l log(e/lambda_l) -> 0, and the threshold constants move by o(1).
(BT) at f_L for L large: F_L = F; carriers with l >= L are peaks with margin >= q_0^L(A_l - theta^L Phi_l) >= q_0^L psi_l Phi_l/2
(theta^L -> theta); carriers with l < L keep u_l(zhat_L) = u_l(zhat) and, as f has no degenerate peaks and theta^L -> theta, keep their
status (strict non-peak with positive gap, or peak with positive margin) — for the finitely many l < L this holds once theta^L is close
enough to theta, which we may ensure by taking L larger (L is chosen after nothing else). Hence Q^L_m is finite, there are no degenerate
peaks, and (MS) holds: sum_{mu < s} Phi <= sum_{psi_l Phi_l < 2s/q_0} Phi_l = o(s) because psi -> infinity and Phi_l decreases
geometrically along each block. QED
*Caveat (honest).* "No degenerate peaks" is used for the finitely many l < L, uniformly in L: the step "take L larger" is legitimate only
if the margins/gaps of the l < L dominate |theta^L - theta| Phi_l; since |theta^L - theta| <= C sum_{l>=L} lambda_l log and Phi_l >= Phi_{L-1}
for l < L, this holds when sum_{l >= L} lambda_l log(1/lambda_l) = o(min_{l<L} (margin or gap of l) Phi_l). If f has margins/gaps decaying
faster along l, choose the A_l (a continuum of choices) so that theta^L = theta exactly — possible by one extra tuning push on a fine
signature set (SKETCH, same genericity issue as 5.5). So: PROVED when f has no degenerate peaks and its small margins/gaps decay no faster
than the design's c_l; SKETCH in general.

## 6.2 Corollary (Lemma Z is a pure lower-semicontinuity statement). PROVED given the existence of G-approximants: by 4.2 (PROVED)
when all rooms are positive and B is finite with (H2), (H3); by 6.1 (SKETCH) in general for F finite.
For such f, g in C(f), rho < 1: Lemma Z holds at (f, g, rho) iff dist(rho g, C(f')) -> 0 along SOME sequence f' -> f in G; the sequences
f_L of 6.1 (in R_BT) and, when all rooms are positive, the far lowerings f^L of 4.2 (in R_0^+-) are candidates. In the language of parts 2-4,
every such approximant is a companion of f at distance >~ c_L log(1/c_L) (resp. c_{L+1}), so Theorem E can use it only on windows above
sqrt(c_L); there the coarse carriers l < L keep the rooms of f, and the race of 4.3(ii) is unchanged.

## 6.3 Numerical sanity checks (scripts in ctx/r5/Z3_work/).
 * check_inward.py (Lemma 5.1): 2000 random finite blocks with a degenerate peak; inward moves at the degenerate peak:
   max [(N(W)-1) - bound] = 4.4e-16, max |<W - w, zeta>|/s = 2.3e-13 (no first-order term); the same omega moved OUTWARD has
   (N(W)-1)/|s| >= 2.6e-4 > 0 in all trials (a genuine kink), confirming that the sign condition is what matters, not the gap.
 * check_cost.py (Lemma 3.1): one block, n = 30, norming functionals by the clamp formula certified by N(w) = 1 and <w, zeta> = |zeta|
   (error 1.2e-15); 900 perturbations mixing unweighted-large fine perturbations and small global ones: max L/R = 0.76.
 * check_cost2.py (necessity of the unweighted term): perturbing ONE fine strict non-peak by |dU_k| = 0.1 lambda_k gives
   L/(Delta log(e/Delta)) up to 1.4e8 (median 6.6e5) but L/R <= 3.2: the cost of a companion is governed by
   sum_k min(lambda_k, |u_k(delta)|) (UNWEIGHTED), i.e. exactifying a strict non-peak carrier of room r costs ~ min(lambda, r), not lambda r.
# Z3 part 7 — main obstacle, corrections to the note, next steps

## 7.1 Main obstacle (precise). OPEN.
All proved recovery mechanisms for the SLD operator are WINDOW methods: on a window of n dyadic scales [T_lo, T_hi], every coarse
carrier must be either pinned (frozen error ~ t/r_l, requiring n >~ K = product (or at best max) of 1/r_l) or exactly switched at
the working first row (exact at f, or at a companion f^# whose cost must be o(T_lo^2) = o(4^{-n} T_hi^2) by Theorem E). For a carrier
of room r_l, exactification costs ~ min(lambda_l, r_l) (Lemma 3.1, unweighted; numerically sharp). Hence a carrier whose room lies in
the band T_lo^2 << r_l << 1/n defeats every window method, and for f with infinitely many carriers whose relative rooms decay
super-geometrically but without tower gaps (e.g. r_l = 2^{-l^4} delta°_l) every window contains such carriers. By Proposition 4.2 this
is exactly a lower-semicontinuity question along the far lowerings f^L (or the peak-ifications of 6.1): is dist(rho g, C(f^L)) -> 0?
The single scale responsible is the transition scale t*_l = sqrt(lambda_l r_l) of each band carrier, where its switching
(<= min(t/(q_0 r_l), 6 lambda_l/t)) peaks at ~ sqrt(lambda_l/r_l) = t*_l/r_l.

## 7.2 Corrections / precisions to the note's Remark rem:openZ (O1). PROVED.
 (a) (O1)(i) concerns only INFINITELY many approximately swallowed carriers (Proposition 4.1); with finitely many, Theorems thm:Bpm,
     thm:S apply as they stand, whatever the rate |z_j| -> 1 or the position of the sign changes.
 (b) (O1)(ii): weak bad peaks and near-threshold bad strict non-peaks are obstacles only for infinitely many bad carriers (5.0); bad
     peaks are pinned (additively) by their inverse margins (Theorem 5.4); (H2) and (H3) can be weakened per block (Theorem 5.3).
 (c) "Approximately two-piece data" cannot be fed to Corollary cor:D1 at f: the kink of Remark 1.5 is unavoidable for defects
     proportional to the scale; the right formulation moves the first row (Theorem E) and is then limited by the band (4.3).
 (d) Lemma 1.4: exactifying a d-neutral, approximately resonant carrier at a companion with the same base part destroys its
     d-neutrality by exactly its room; Remark rem:thmM's "finitely many inexact coordinates (equations instead of inequalities)" works
     only while the inexact coordinates are finitely many AND the d-rows stay well conditioned.

## 7.3 Next steps (suggested).
 1. Lower semicontinuity along far lowerings f^L at (W+-)-failing points: compare the two-sided decompositions of g at f and at f^L
    scale by scale; the fine carriers l > L are pinned at f^L with GOOD constants, so the question is whether g's switching through
    l > L (at scales <= C lambda_l <= C c_{L+1}, far below the slack threshold sqrt(c_{L+1})) can be replaced at f^L by two-sided block
    usage at second-order cost — this needs the switching amplitude through l to be o(1) at those scales, a statement about g, not f.
 2. A multi-level averaging in which a band carrier's frozen error enters through log(1/r_l): average separately the scales below and
    above t*_l and glue with the slack of a SECOND parameter (two nested windows); the obstruction in 4.3(ii) is a single scale per carrier.
 3. Re-tuning the Hilbert part (4.3(iii)) to make the companion cones of d-neutral approximately resonant carriers non-degenerate.
 4. The tuning lemma for degenerate peaks (5.5(ii), 6.1): a first-order genericity statement for the clamp equation of a block.
 5. Shifted (infinitely supported) two-piece data for (H2)-failing blocks with non-d-neutral switching (5.6(b)), in the spirit of the
    shifted certificates of Section sec:certificates.
