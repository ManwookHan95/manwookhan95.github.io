# V3 referee, part 1: Section 2 (raise transfer, Theorem E_RT) and Section 1

Sources re-read: V3_notes.md, V3_part1..4.md, V3_work/rt_check.py; note lem:dualball, lem:threshold, prop:forced,
prop:approximants, rem:lemmaZ(c), lem:slack, lem:twosided, lem:smallness, lem:budget, lem:suplevel, lem:box, def:windowcert,
prop:windowcert, lem:uniformtransfer, lem:TV, prop:rebalancing, lem:transferdata, lem:persistence, def:twopiece,
lem:switchbudget, lem:modswallow, lem:badpeaks, lem:exactswitch, lem:windowtwopiece, lem:onesidedtransfer, lem:avgfunctionals,
thm:windowed, def:SLD, thm:SLD; Z5_ref_notes (R1, R2); Z3_notes 3.1 (cost of a companion) + Z3_ref 2.1; Y3_notes 2.1, 3.5;
Y3_referee, Y3_ref_notes 3.2-3.4.

## Lemma 2.1 (basic facts). CORRECT.
(a) same signs on F give ||a + Da||_1 = ||a||_1 + ||Da||_1; triangle inequality in H. (b) ||x/|x| - y/|y| || <= 2||x-y||/|y|.
(c) zhat^# - zhat = U(e^# - e). (d) a^# - a = Da/lam + (1/lam - 1)a, |1 - 1/lam| <= lam - 1 <= ||Da||_1 + ||U*Da||.
Convergence f^# -> f: argument of prop:approximants (ii)=>(i) for forced-data rows (rem:lemmaZ(c)); z fixed, a^# -> a in l_1. OK.

## Lemma 2.2 (normer change). CORRECT.
w_m = J_m(R_m** zhat) by 0-homogeneity of J_m, so w^# - w depends only on delta = zhat^# - zhat = U(e^# - e); Z3 Lemma 3.1 (refereed,
upper bound) uses only the clamp formula at zhat, zhat^# and applies verbatim. |u_k(delta)| <= ||U*u_k|| ||e^# - e|| <= ||U|| ||e^#-e||
(||U*u|| <= ||U|| ||u||_1 <= ||U|| q*(u)). Delta_m <= m 2^{-m} eps_e; x log(e/x) increasing on (0,1]; counting bound. OK.
Precision: the bound is p*(L*(w^# - w)) <= C eps_e log(e/eps_e) with C an f-constant, valid once eps_e <= c_f.

## Lemma 2.3 (RT). CORRECT (re-derived).
Key identity: a^# + rB = (A + Da)/lam, so q*(a^# + rB) <= (q*(A) + ||Da||_1 + ||U*Da||)/lam, and ||Da||_1 <= lam - 1 + ||U*Da||
(lower bound in 2.1(a)); blocks: w + r Theta = (1 - 1/lam) w + W/lam (convex combination, needs lam >= 1). The raise mass
cancels exactly against lam - 1. Nothing requires pi >= 1 or smallness of ||Da||_1. With a VP correction Da'' on F_0 (|Da''| <= |a|/2):
||a + D||_1 >= ||a||_1 + ||Da||_1 - ||Da''||_1, extra error 2||Da''||_1: CORRECT.
Interpretation (for the record): the raise changes the excess function of every direction only by the RELATIVE factor
1/lam inside and lam outside (p*(f^# + rh) - 1 <~ (p*(f + lam r h) - 1)/lam), i.e. the quadratic coefficient of a mate becomes
lam (1 + O(||Da||_1)), not "1 + additive ||Da||_1". This is the genuinely new observation of V3.

## Corollary 2.4. CORRECT.
phi(lam) = (s(lam x) - 1)/lam, phi' = (s(u) - 1)/(lam^2 s(u)) <= min(x^2/2, 1/lam^2) (even slightly better than stated).

## Theorem 2.5 (E_RT). CORRECT (all constants re-derived).
Case |r| <= r_0, I_r nonempty: rho|r| > c_flat T 2^{1-n} gives eps' < theta rho^2 r^2/4; (lam-1)lam^2 rho^2 r^2/2 <= (1-rho^2)r^2/48;
K-term <= (1-rho^2)r^2/24; sum <= (1-rho^2)r^2/12; then 1 + r^2(2+rho^2)/6 <= 1 + r^2/2 - r^4/8 needs r^2 <= 4(1-rho^2)/3: OK.
Case |r| > r_0: three terms each <= (1-rho^2) r_0|r|/48 and min(r^2,|r|) >= r_0|r|: OK. (c) K_j T_j -> 0 gives the convergence.
Remark: with f_j = f this is thm:windowed + lem:avgfunctionals; with lam = 1, eps' = p*(f_j - f), Z3 Theorem E at arbitrary F.

## Section 1. Lemma 1.1: CORRECT identity (constant: |r_pm(s)| <= (2/(3t)) 2^{-2s} c_l delta_l suffices; the qualifier "beyond
coarser targets" is vacuous since coarser targets never meet S_l by allowedness (a)). Model 1.2: computation re-derived:
int_0^{v_s} m_v = 2v_s^2/3, Phi(v_s(1+u)) = 2(2/3 + 2u)/(1+u)^2 in [4/3, 3/2], max at u = 1/3. CORRECT.
The interpretive sentences ("the referee's factor 2 is a property of R1's deep assignment", "copied data lose only 9/8")
are HEURISTIC: copying B_pm on the deep set produces data whose difference is Delta B, not the exact switching X, and the
consistency/exactness of such copied data is not proved; but Y3_ref 3.2 itself calls the factor 2 a statement about deep
assignment ("statements about what the method certifies"), so there is no contradiction. Remark 1.3: CORRECT (thm:compact).
