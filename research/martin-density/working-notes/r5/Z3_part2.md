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
