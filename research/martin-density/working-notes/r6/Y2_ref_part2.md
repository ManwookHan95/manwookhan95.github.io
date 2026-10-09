# Y2 referee, part 2: Proposition Q (companion transfer) and Corollary Q'

## Proposition Q. Verdict: CORRECT (PROVED), with one statement precision (P-Q1) that the later uses need.
Checked step by step against Remark rem:lemmaZ(c), Lemma lem:threshold, Lemma lem:algebra, Definition def:twopiece, Theorem SLD
(P1), allowedness (a),(b), Z3 Theorem E and Lemma U' (part 1).

Step 1 (companion). (a, z + delta) with |z + delta| <= 1, z + delta = sgn a on F is admissible forced data (rem:lemmaZ(c)); the forced
data of f_j are a_j = a, e_j = e, nu_j = nu, zhat_j = zhat + delta, w_{j,m} = J_m(R_m^** zhat_j). ||R_m^**(zhat_j - zhat)||_1 <=
sum_k lambda_{k,m} |u_{k,m}(delta)| <= |I_D| max eta; weak* cluster points of w_{j,m} norm R_m^** zhat, so equal w_m by smoothness;
D_m w_{j,m} -> D_m w_m (dominated convergence, Phi in l_2), L^*w_j -> L^*w (L compact). CORRECT.
Step 2 (thresholds rise). The donor coordinate k'_m of block m changes ONLY through its own move: s_{m'} (m' != m) lies outside
supp y_{l'_m} (s_{m'} notin X_j) and, by (P1), u_{l'_m}(s) = 0 for s in S_{l'} with l' > l'_m. Other changes of zeta_m come from
targets of later carriers; allowedness (b) and lambda_l <= c_l/4, ||y||_inf <= 1, n_l >= 3/4, sum_{l >= L} c_l <= (4/3)c_L give
E_m <= sum_{m'} (2/9) 2^{-2 s_{m'}} c delta eta <= |I_D| 2^{-r} Delta (with Delta_{m'} >= (4/5) 2^{-m'-k'-s} c delta eta). Lemma T(e) then
gives theta(zeta') > theta(zeta) for every common Delta > 0 once N 2^{-r} < min(A/(A+theta), nu_{k'}/(2(A+theta))). Re-derived; CORRECT.
Step 3. (a) used switching carriers keep their values: s_{m'} lies in the signature set of a donor (not in Sw_j, so in no S_l, l in Sw_j)
and outside T_j, hence u_l(s_{m'}) = 0 for l in Sw_j by (P1). (b) Every used inward coordinate is a SWITCHING coordinate: if
omega^+(k) = omega^-(k) at an inward k then varsigma omega^+ <= 0 <= varsigma omega^- forces both to vanish. Hence nu'_k = nu_k = theta(zeta) <
theta(zeta'): k is a strict non-peak of f_j, with the same sign (zeta'(k) = zeta(k) != 0). (d) d-coefficients: off P (and at degenerate
peaks, alpha = 0) Phi^2 w(k)/C = zeta(k)/|zeta|; at f_j the same with zeta'(k) = zeta(k) on supp(omega^- - omega^+); so
d^{(j)}(omega^- - omega^+) = (|zeta|/|zeta'|) d(omega^- - omega^+) = 0, and b^+ - b^- = sum R^*(omega^- - omega^+) is first-row free.
(f) b^+-(zhat_j) = 0 because supp b^+- avoids {s_m}; b^-(xi_j) = b^+(xi_j) by Lemma lem:algebra at f_j (all used coordinates are strict
non-peaks of f_j). (g),(h),(i): finitely many fixed data, continuity. Step 4: Theorem E' with K_j + 1. All CORRECT.
Quantifiers: window data are built from (g, rho); for each window the companion is chosen afterwards with Delta_j -> 0; Lemma U' gives
(t_1, j_0) for the resulting sequence (j_0 depends only on the convergence f_j -> f, which is ours); c_{flat,j} from (A_2(j), gamma_B(j)).
No circularity. Lemma Z is per mate, as required.

(P-Q1) PRECISION (needed by Theorem P(b) and Theorem Y). As stated, (W2) allows inward coordinates only at DEGENERATE PEAKS of f and (W4)
requires gap conditions at all other used coordinates. The window data of Theorem U' (Z6 referee Lemma 2.1, "shift trick") use kept q > 0
strict non-peaks INWARDLY with arbitrarily small gap (third kind). Fix (PROVED): allow in (W2) inward coordinates that are degenerate peaks
or strict non-peaks of f (any positive gap), with |omega| <= A_2(j)/t there. In the proof only Step 3(b) changes: a used inward strict
non-peak k of f is a switching coordinate (same argument), so nu'_k = nu_k < theta(zeta) when k lies in a block of I_D (threshold raised),
and in a block outside I_D it stays a strict non-peak of f_j for Delta small by continuity (finitely many coordinates, each with positive
gap at f; the sign is unchanged since zeta'(k) = zeta(k)). Either way it is a kind-[3] coordinate of Lemma U' at f_j. d-neutrality is
unaffected (Step 3(d) used only that the coordinates of supp(omega^- - omega^+) are switching and strict non-peaks at f_j).

Adversarial checks attempted (none breaks the proposition): cross-block interaction of several donors (handled: X_j and (P1));
donor inside Bl_j \ Sw_j (its value moves by Delta + E_m -> 0; it cannot be an inward coordinate); unused degenerate or weak peaks of f
becoming non-peaks at f_j (irrelevant: data vanish there; transfer peaks have positive margins and persist, Lemma lem:persistence);
blocks outside I_D whose threshold may DROP through targets (only finitely many used coordinates, all strict non-peaks with positive gap,
so continuity suffices); Theorem E's uniformity (t_1, j_0 independent of A_2(j), gamma_B(j): part 1); c_0 vs l_infty (f_j need not attain
its norm; Corollary cor:D1 is applied at f_j to fixed averaged data, and its engineered approximants truncate); the d-coefficient at an
inward coordinate at f_j uses w_{j,m}(k) off P^{(j)}, which is the clamp value C_j zeta(k)/(Phi^2 |zeta'|): consistent.

## Corollary Q'. Verdict: CORRECT (PROVED).
With fixed data, (W3)-(W5) hold for t <= 1 with g_t := g, A_2 := 1 + max|omega^+-|, gamma_B := least gap of supp omega^+- \ D at f (> 0,
finitely many coordinates), K_j := 1; c_flat is then fixed, (E-d') reads n_j >= const, true for n_j = j; (E-e') is a choice of Delta_j.
The donor hypothesis is stated with supp b^+ ∪ supp b^- removed, which covers base parts with infinite support on K (general two-piece
data need not have the SLD window structure). Kappa_w <= 1 gives Gamma^{(j)}_w <= 1 + eta_0/2 for Delta_j small.
Comment: Corollary Q' is the cleanest form of the new mechanism: the companion turns every used degenerate peak into a strict
non-peak with a tiny but FIXED gap, and Corollary cor:D1 at f_j chooses its scale s_1 after f_j, so the averaged datum omega^theta,
outward on one side at k, is harmless at f_j (this is exactly what Z4-referee Observation 9.1 required, mu'_k <= -kappa_D s_1, and it now
holds because s_1 -> 0 at fixed f_j). The steering problem at engineered approximants of f is thereby bypassed, not solved.
Scope: SLD-type designs (private signature coordinates are what makes the donor move invisible to the used carriers).
