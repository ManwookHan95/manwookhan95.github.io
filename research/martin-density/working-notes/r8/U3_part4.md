# U3 part 4 — Recovery of (C*) rows: quadratic banks, violation tolerance, and the precise remaining steps

Setting: D^{V2} on D_Omega with diagonal U (+ V4's (SF*), (SF_tau), (b'), (Z0) where cited), finite I, F finite, g in C(f), rho < 1.
"Exact data" = two-piece data of Definition def:twopiece.  A VIOLATION of a pair (b, omega) at a coordinate j notin F is the amount
by which side admissibility fails there: viol^+(j) := |b(j)| if j is free, := (z_j b(j))_- if j is a contact (side +; symmetric for
side -).  ||viol|| := sum_j (viol^+(j) + viol^-(j)).

## 4.1 Lemma QB2 (a bank turns a linear violation into a quadratic cost).  PROVED (any admissible T).
Let f have F finite, let E be a finite set of contacts, and let f^b be the row with forced data (a^b, z) where
a^b := (a + sum_{j in E} m_j z_j e_j^*)/q*(a + sum_{j in E} m_j z_j e_j^*), m_j > 0 (z unchanged; z_j = sgn a^b_j on E, so the data
(a^b, z) are admissible, Remark rem:lemmaZ(c)).  Then F^b = F ∪ E and, for every B in l_1 and t in R,
     Exc^b(t B) <= Exc^{b,0}(t B) + sum_{j in E} t^2 B_j^2 / (2 |a^b_j|),
where Exc^{b,0} is the excess functional of Lemma lem:bookkeeping(b) with the summands at j in E omitted (they are the flip terms).
Pairs (b, omega) that are side-admissible off E and ARBITRARY on E are two-piece data at f^b (E ⊂ F^b), so Proposition
prop:onesidedupper applies at f^b as stated (as t -> 0 no flip occurs).  The point of the lemma is UNIFORMITY in the bank masses: in
the proofs of Proposition prop:onesidedupper, Lemma U (Z3) and Theorem thm:engineered, the condition "no flip on F" (e.g. (T_1):
rho T_0 (||b^+||_inf + ||b^-||_inf) <= a_min/8) may be imposed on F only, the flip part on E being bounded instead by
(t^2/2) sum_E B_j^2/|a^b_j|; the scale range T_0 is then independent of the masses, and Gamma_w is replaced by
     Gamma^E_w(b, omega) := Gamma_w(b, omega) + q^b_0 sum_{j in E} b_j^2 / |a^b_j| .
Proof.  On F^b the excess summand is 2(-sgn(a^b_j) t B_j - |a^b_j|)_+ (Lemma lem:base); for x >= 0 and m > 0, 2(x - m)_+ <= x^2/(2m)
(the parabola x^2/(2m) - 2(x - m) = (x - 2m)^2/(2m) >= 0), and the summand is 0 when -sgn(a^b_j) t B_j <= 0.  In each of the cited
proofs the flip part of Exc enters only through an upper bound hat G_b for the base excess, and the rebalancing step (Proposition
prop:rebalancing) accepts any upper bound hat G_b.  QED
Quantitative consequence (choice of masses).  Given violations e_j := b(j) (j in E) of total mass epsilon := sum_E |e_j| and a budget
beta > 0 in Gamma, the masses m_j := (q_0 epsilon/beta) |e_j| (times the normalising factor) give q^b_0 sum_E e_j^2/|a^b_j| <= beta(1 + o(1)),
and the companion moves by p*(f^b - f) <= C_f sum_E m_j = C_f q_0 epsilon^2/beta: QUADRATIC in the violation.  Numerical check
(U3_work/vt_check.py, finite N = 1 model, dead-zone contact touched by no carrier, rho = 0.9): the least bank mass that makes
rho g_e a mate is m_min = 1.33e-5, 3.16e-6, 7.50e-7, 1.78e-7 for epsilon = 4e-3, 2e-3, 1e-3, 5e-4, i.e. m_min/epsilon^2 = 0.83, 0.79,
0.75, 0.71 (prediction for kappa_w ~ 0: m_min ~ rho^2 epsilon^2 = 0.81 epsilon^2), and p*(f^b - f) ~ 2 m.

## 4.2 Lemma VT (violation tolerance of the engineered approximants, single stage).  PROVED.
(A line-by-line modification of the proof of Theorem thm:engineered in the note; nothing else is used.)
Setting.  I finite, f in S_{p*} with F finite, rho in (0,1), g in X^* with g(xi) = 0.  Let (b^+, omega^+), (b^-, omega^-) be pairs that
REPRESENT g in the sense of Definition def:twopiece (g = b^+- + sum_m R_m^*(omega^+-_m - d_m(omega^+-_m) w_m), omega^+-_m in c_00,
supp omega^+-_m in Q_m), but are NOT assumed side-admissible.  For j notin F put
   viol(j) := (z_j b^+_j)_- + (z_j b^-_j)_+   if j in K (contact),      viol(j) := |b^+_j| + |b^-_j|   if j notin F u K (free),
and epsilon := sum_{j notin F} viol(j) (<= ||b^+||_1 + ||b^-||_1).  Two-piece data are exactly the case epsilon = 0.  Hypotheses:
 (H1) rho^2 kappa_w < 1, kappa_w := max(Gamma_w(b^+, omega^+), Gamma_w(b^-, omega^-)) (the formula of def:twopiece);
 (H2) I_- := {m : Delta d_m < 0} satisfies (SC) (no assumption if I_- is empty);
 (H3) (theta-exactness at free coordinates of the window) b^+_j + b^-_j = 0, i.e. b^theta_j = 0, at every free coordinate
      j <= N_w with viol(j) > 0 (for instance: at every violated free coordinate).
Statement.  Choose delta, T_1, K_sharp, eta_1, the transfer data and T_0 exactly as in Step 0 of the proof of thm:engineered for the data
(f, b^+-, omega^+-, rho), except that K_sharp is replaced by K_sharp + 1.  Let (N_w, s_1, N'') be a stage of the construction sequence of
that proof which is late in the sense of that proof — i.e. the explicit inequalities used in Steps 1-5 hold at it: (N1)-(N3), persistence
of the transfer data, |lin'_m| <= K_sharp |tau| s_1, hat G_b, hat G_m <= K_sharp tau^2, the bracket bound Gamma_diamond + delta/8, and
(1/2) rho |tau| V_{>N''} + |tau| o(s_1) <= delta tau^2/16 for |tau| > s_1 — and at which (H3) and
     (VT)   2 rho epsilon <= delta s_1 / 16
hold.  Then the engineered approximant f' (Definition def:engineered; norm-attaining) and g' := rho(g'' - c a') of Step 1 satisfy
     p*(f' + tau g') <= 1 + (tau^2/2)(1 - delta)      for 0 < |tau| <= T_0.
Proof.  (1) Where admissibility is used.  Step 0 uses the data only through kappa_w (Gamma_theta <= kappa_w by convexity; (H1)) and
through the finitely many constants listed there; Step 1 and Step 2 use only the two representations (g'' - g -> 0, g'(x-hat') = 0,
the identities beta^+- - beta^theta = +-(1/2)v, v = b^+ - b^- = sum_m R_m^*((omega^-_m - omega^+_m) - Delta d_m w_m)); Step 3 (Blocks)
uses only supp omega^diamond_m in Q_m and the radius conditions; Lemma lem:approxfacts uses b^theta only through the masses
m_j = 4 rho s_1 |b^theta_j| and ||b^theta||_1.  The sign conditions on b^+- enter ONLY the claim of Step 3 (Base),
Exc'(tau B^diamond) <= (1/2) rho |tau| V_{>N''} (and = 0 for diamond = theta).  We replace it by
     Exc'(tau B^diamond) <= (1/2) rho |tau| V_{>N''} + 2 rho |tau| epsilon   (diamond = +-, s_1 < |tau| <= T_0),
     Exc'(tau B^theta) = 0                                                (0 < |tau| <= s_1).                          (*)
(2) Proof of (*).  By Lemma lem:bookkeeping(b) at f', Exc'(B) = sum_j (|a'_j + B_j| - |a'_j| - z'_j B_j); on supp a' the summand is
2(-sgn(a'_j) B_j - |a'_j|)_+, off supp a' it is |B_j| - z'_j B_j.  With B = tau B^diamond = tau rho(beta^diamond - c a'):
 on supp a', a'_j + tau B_j = (1 - tau rho c) a'_j + tau rho beta^diamond_j with 1 - tau rho c >= 1/2, so the summand equals
 2(-x - (1 - tau rho c)|a'_j|)_+ <= 2 (x)_- with x := z'_j tau rho beta^diamond_j.
 * j in F: no flip by (T_1), summand 0 (unchanged).
 * window contact with mass (j in K, j <= N_w, b^theta_j != 0; z'_j = z_j): diamond = theta: |tau rho b^theta_j| <= m_j/4 <= |a'_j|/2,
   summand 0 (for either sign of b^theta_j).  diamond = +: tau > 0, x = tau rho z_j b^+_j, summand <= 2 rho |tau| (z_j b^+_j)_-.
   diamond = -: tau < 0, x = -|tau| rho z_j b^-_j, summand <= 2 rho |tau| (z_j b^-_j)_+.  In both cases <= 2 rho |tau| viol(j).
 * window contact without mass (b^theta_j = 0, so beta^theta_j = 0 and b^+_j = -b^-_j): off supp a'; diamond = theta: 0;
   diamond = +: |tau rho b^+_j| - z_j tau rho b^+_j = 2 rho |tau| (z_j b^+_j)_-; diamond = -: = 2 rho |tau| (z_j b^-_j)_+; <= 2 rho |tau| viol(j).
 * free j <= N_w: off supp a', |z_j| <= 1; diamond = theta: beta^theta_j = b^theta_j = 0 if viol(j) > 0 by (H3), and b^+-_j = 0 if viol(j) = 0;
   summand 0.  diamond = +-: summand <= 2 rho |tau| |b^diamond_j| <= 2 rho |tau| viol(j).
 * contact j in (N_w, N'']: beta^theta_j = 0; beta^+-_j = +-(1/2) v_j, so for diamond = sgn tau, tau beta^diamond_j = (1/2)|tau| v_j and the
   summand is rho |tau| (z_j v_j)_-.  Since z_j v_j = z_j b^+_j - z_j b^-_j >= -(z_j b^+_j)_- - (z_j b^-_j)_+, (z_j v_j)_- <= viol(j).
 * free j > N_w: beta^theta_j = 0; |beta^+-_j| = |v_j|/2 <= viol(j)/2; summand <= 2 rho |tau| |v_j|/2 <= rho |tau| viol(j).
 * contact j > N'': z'_j = 0, summand rho |tau| |v_j|/2 (diamond = +-) and 0 (theta): this is the term (1/2) rho |tau| V_{>N''} (unchanged).
 Summing gives (*).  (Free coordinates are never in supp a' = F u {window contacts with b^theta != 0}.)
(3) Constants.  For |tau| > s_1, (VT) gives 2 rho |tau| epsilon <= delta |tau| s_1/16 <= delta tau^2/16 <= tau^2/32, so the bound
hat G_b <= K_sharp tau^2 of Step 0 holds with K_sharp + 1, and Step 4 (rebalancing, |varepsilon_m| <= 6 K_sharp tau^2, error E <= delta tau^2/8 by
the choice of eta_1 with the new K_sharp and the (T_0) conditions) is unchanged.  K_A (bound for (|q*(A_tau) - 1| + q*(A_tau - a'))/|tau|) is
finite since beta^diamond in l_1; it is chosen before T_0 as in the note.
(4) Step 5.  hat Gamma = c' hat G_b + sum_m sigma'_m hat G_m gains at most c' 2 rho |tau| epsilon <= delta tau^2/16 (c' = 1/p(x-hat') <= 1) in the
+- regimes and nothing in the theta-regime.  Hence, for 0 < |tau| <= T_0,
     p*(f' + tau g') <= 1 + (tau^2/2)(rho^2 kappa_w + delta/8 + delta/8 + delta/8 + delta/4 + delta/8) = 1 + (tau^2/2)(1 - 2 delta + 3 delta/4)
                     <= 1 + (tau^2/2)(1 - delta).   QED
Remarks.  (a) In-window CONTACT violations need no bank when (VT) holds: their cost is the same linear 2 rho |tau| viol(j), paid only
for |tau| > s_1 (in the theta-regime the masses m_j protect every window contact, whatever the sign of b^theta_j).  Banks (Lemma QB2)
are needed only for violations whose mass is NOT <= delta s_1/(32 rho) at an admissible s_1.
(b) Free violations inside the window with b^theta_j != 0 are NOT tolerated: they cost 2 rho |tau| |b^theta_j| for |tau| <= s_1, which is
not O(tau^2); free coordinates cannot carry masses (that would change z'_j from |z_j| < 1 to +-1, an O(1) move of x-hat').  This is the
reason for (H3).
(c) What the lemma does NOT give.  Step 6 (Lemma lem:assembly) needs a pair (f_0, g_0) with g_0 in C(f_0) and p*(f' - f_0) <=
(1 - rho^2) T_0^2/6, p*(g' - rho g_0) <= (1 - rho^2) T_0/6.  A functional with violated data is in general NOT a mate of f (U3_work/
vt_check.py: positive excess at f), so in applications the assembly is made relative to the ORIGINAL pair (f_0, g_0) = (f, g) of the
(C*) row, which needs T_0 (of the violated data at the companion) to be large compared with sqrt(p*(f' - f_0)): a uniformity statement.
Moreover (VT) bounds s_1 from below, while "late" means s_1 below a threshold s_late(data) (Bx_m = o(s_1), (E4) convergence, scrambling):
the lemma is useful iff epsilon <= delta s_late/(32 rho).  Both points belong to (S2), see 4.3 and 4.3'.

## 4.3 Proposition RT* (structure of the shifted transplant in case (II)).  PROVED parts and SKETCH parts as marked.
Let w be a clean sub-window of level l in case (II) (rho^sh(kappa, f) <= b(w), c_pi(w) <= b(w)), I_sh the source-deficient blocks.
 (a) (PROVED, V2 Corollary C1.1(a)) The COMBINATORIAL coherent resonance is EXACT: c^comb_*(kappa) = 0, i.e. there are delta on the sign
     sphere of I_sh and x >= 0 on the class-G strict non-peaks with sum_m delta_m Pi_m + sum x eps u zero-cost on the coarse target
     coordinates T(l) and without sign defect on the natural signature sets.  (If c^comb_* > 0 it is >= delta_sh(l) > C Design(l) b(w)
     and case (I) holds.)
 (b) (PROVED, Lemma A of Part 2 and its multi-block form Lemma S) Exact shifted data exist at a row f' iff, outside the supports of
     the omega-carriers, W_Delta = sum_m Delta_m psi'_m vanishes at the free coordinates and is (-z')-signed at the contacts; the
     functional (split chi, omega^+, base part on F) is otherwise free.
 (c) (SKETCH) At V1's companion f^# of w (exactifications (C1)-(C4), donor raise Lambda = T_lo^3, aligned fine re-alignment beyond a
     level L' >> l, Proposition 5.3 of V4), the conditions of (b) hold on all COARSE coordinates for every shift delta in the exact
     combinatorial cone of (a) (owners of coarse coordinates are coarse; peaks of shifted blocks carry the coefficients of (a); coarse
     strict non-peaks are omega-carriers and are bumped where their coefficient vanishes, Lemma 3.5 of Part 3), EXCEPT for: (i) the
     coupling rows Delta_m = d_m(omega^-_m) - d_m(omega^+_m) (V2's (C*-3)), and (ii) contributions of carriers > l at coarse coordinates
     ("medium" carriers l < c <= L' and "fine" carriers c > L'), whose total l_1-mass is at most C |Delta| sum_{c > l} lambda_c <= C |Delta|
     T_lo(w)^3.
 (d) (PROVED given (c)) All violations caused by carriers c > l (medium carriers touch coarse coordinates only through their finitely
     supported targets — allowedness (a) keeps coarse targets off S_c — but an anti-aligned medium carrier also violates on its own
     infinite signature set S_c; fine carriers c > L' violate anywhere) have total l_1-mass epsilon <= C |Delta| sum_{c > l} lambda_c <=
     C |Delta| T_lo(w)^3 and are summable over coordinates.  Hence for every epsilon' > 0 all but epsilon' of this mass lies on a finite set
     E of contacts (heads of the signature sets carry almost all of their mass: v_c(s) = delta_c 2^{-s}/n_c).  Banks of Lemma QB2 on E with
     total mass <= C epsilon^2/beta <= C (|Delta| T_lo^3)^2/beta = o(T_lo(w)^2) absorb these violations into Gamma^E at an extra cost beta;
     the tail epsilon' is left to Lemma VT.  (By Remark 4.2(a) in-window contact violations may instead be tolerated directly when
     their mass is <= delta s_1/(32 rho).  Free coordinates cannot be banked; violations at FREE coordinates are of fine origin only —
     coarse free rows are exact by (c) — and Lemma VT tolerates them beyond N_w automatically and inside the window under (H3).)
 (e) (SKETCH) With Lemma VT at the banked companion (s_1 chosen in a scrambling gap below Lambda, with 32 rho epsilon'/delta <= s_1 <=
     theta T_lo^2) and the averaging of Z3 Theorem E carried out AT the engineered approximant (4.3'(S2b): pieces at the scales of w;
     bound (A) via the engineered transfer of each piece up to its own radius, bound (B') via closeness to (f, rho g)), one obtains NA
     pairs converging to (f, rho g).  Mixed signs of Delta_m across blocks
     are allowed by Theorem thm:engineered ((SC) is needed only for blocks with Delta_m < 0 and holds at the companion along gap scales).
 (f) (Scale bookkeeping; PROVED arithmetic, assuming the design strengthening (W10): c_{l+1} <= T_lo(l)^{10}, an upper bound on
     weights that every SLD-type design admits by V4 Lemma 2.1's argument — window theorems use weights only through upper bounds.)
     Violations at FREE coordinates cannot be banked; they have total mass <= C |Delta| sum_{c > l} lambda_c <= C |Delta| T_lo(l)^{10}.
     Lemma VT needs s_1 >= 32 rho (that mass)/delta, while the scrambling estimate at the companion needs s_1 below the donor raise
     Lambda = T_lo^3 times the least coarse weight and inside a gap of the weight sequence; both hold for s_1 := T_lo(l)^{8} c_l (say),
     since T_lo(l) <= 2^{-n^w_l} T_hi(l) is super-exponentially smaller than c_l >= T_lo(l-1)^{10}.  Without (W10) (c_{l+1} ~ T_lo^3) the
     two requirements collide (free-coordinate violations ~ Lambda): this is the precise reason why V2's (C*-1) looked like an exactness
     problem; with (W10) it becomes a bookkeeping problem.
Consequently (C*) reduces to two precise steps, both finite-dimensional or local:
 (S1) [coupling exactness] at the companion, the coupling rows Delta_m = d^#_m(omega^-) - d^#_m(omega^+) can be satisfied EXACTLY
      inside the exact combinatorial cone of (a) with a design x u^{-O(1)} Hoffman constant.  For N = 1 (or a single shifted block)
      this holds whenever some class-G strict non-peak k with q_k < 0 of the shifted block has its column x_k eps_k u_k as a free ray of
      the zero-cost cone (its target coordinates in T(l) are contacts dominated by their owners or lie in F) — e.g. V4's l_- with
      target y* on F — because increasing x_k changes sum q x without changing delta (PROVED).  In general it is a single equation per
      shifted block whose coefficients are values; per-carrier exact tuning (Y4-ref Prop. P4 / V1 Lemma TU) of one value per block
      solves it as soon as its derivative is bounded below, a quantity that can be made a rate object of the design (SKETCH).
 (S2) [uniform composition] Lemma VT is now PROVED at a single stage (4.2); what remains is the uniform composition (e), made
      precise in 4.3' as (S2a)-(S2d).
Neither step involves an f-dependent rate beyond those already absorbed by the window recursion (modulo the exponent bookkeeping
(S2c)), and nothing in (C*) obstructs them.

## 4.3' The precise content of (S2).
 (S2a) [Lemma U^eng: uniform per-piece engineered bounds] SKETCH.  For pieces (b^+-_t, omega^+-_t) at scales t obeying the size
      conditions of Z3 Lemma U (t ||b||_1 <= A_0, Gamma_w <= 2, |omega_m(k)| <= 2 gap/t, or <= A_2/t where gap >= gamma_B) and violations
      of mass epsilon_t, the constant T_0 of the proof of thm:engineered (with Lemma VT) can be taken >= c_flat t, with c_flat independent of
      t and of the row along a convergent family of rows with base support F u E (bank coordinates E handled by Lemma QB2, so a_min is
      needed on F only).  Scaling check (PROVED arithmetic): every condition (T_1), (T_0) has the form T_0 X <= Y with X = O(1/t) and Y
      bounded below: |Delta d_m| <= A_2 ||D_m||^2/(t C_m)-type bounds, ||b^+-||_inf <= A_0/t, coordinatewise radius of omega >= t/4 (size
      conditions), K_W ~ ||Omega^diamond|| = O(1/t), and the error terms 6|I|K_sharp K_Y |tau|^3 K_A and 48 K_sharp K_W K_y |tau|^3/(min C/2)
      with K_A, K_W = O(1/t) are <= delta tau^2/32 for |tau| <= c t; K_sharp = O(1) because Gamma_w <= 2 bounds the quadratic terms.
      Not checked line by line: uniformity in t of the data-dependent late-stage thresholds ((E4) has constant K(omega) = O(1/t)).
 (S2b) [Theorem E^eng: averaging at the engineered approximant] SKETCH (given (S2a)).  For a companion f_j and its finitely many
      pieces g_{j,t_i}, take one stage that is late for every piece, with masses m_j := 4 rho s_1 max_i |b^theta_{i,j}| (Lemma
      lem:approxfacts is unchanged with larger masses) and N'' satisfying (N3) for every piece.  Then f'_j is an engineered approximant
      for every piece simultaneously, and g'_j := (1/n) sum_i g'_{j,i} (Step 1 is linear in the data).  The averaging argument of Z3
      Theorem E runs at f'_j: (A^eng) p*(f'_j + tau g'_{j,i}) <= 1 + (tau^2/2)(1 - delta_*) for |tau| <= c_flat t_i (Lemma VT + (S2a));
      (B'') p*(f'_j + tau g'_{j,i}) <= s(rho tau) + p*(f'_j - f) + |tau| p*(g'_{j,i} - rho g) (g in C(f)); scale decoupling
      p*(f'_j - f) <= theta_j (T_j 2^{-n_j})^2.  Conclusion: g'_j in C(f'_j), f'_j norm-attaining, (f'_j, g'_j) -> (f, rho g).  This replaces
      the final non-uniform call of Theorem E to Corollary cor:D1 (which needs exact data) by a single uniform stage.
 (S2c) [threshold comparison] HEURISTIC.  Lemma VT at the companion f^#_w needs epsilon_w <= delta s_late(f^#_w)/(32 rho).  The row-
      dependent part of s_late (Bx_m = o(s_1) and the scrambling estimate) involves sum_k lambda_k |w'_m(k) - w_m(k)|, which is controlled
      by the gaps of the companion at the levels <= L(eta) where the weight tail drops below eta/4 — a FIXED set of levels, so this part
      is uniform in l as the companions converge to f.  The data-dependent part ((E4) with K(omega) ~ 1/(t gap_min(levels <= l)), and the
      convergence of h', H') gives s_late >~ t gap_min(<= l); with t ~ T_lo(w), exactified gaps at companions >= T_lo^{O(1)} (V1 (C1)-(C4))
      and epsilon_w <= C |Delta| T_lo^k under the design strengthening (W_k): c_{l+1} <= T_lo(l)^k, the comparison holds for k large
      enough.  To be checked: the exponents of V1's exactifications against k.
 (S2d) [free violations] SKETCH.  Violated free coordinates beyond N_w are tolerated automatically (symmetric split of the construction);
      inside the window (H3) is needed.  Far free coordinates (j > J) can moreover be CONVERTED into contacts: replacing z_j (|z_j| < 1) by
      +-1 keeps z' in the subdifferential of ||.||_1 at a (j notin supp a), keeps q(z' + Ue) = 1 (as in Lemma lem:approxfacts(a)), and moves
      R_m x-hat by at most 2 t(J) -> 0 (t(J) = sum_k lambda_k ||u_k 1_{(J,inf)}||_1), so the converted rows converge to the companion
      (Proposition prop:continuity); the converted coordinate is admissible on both sides iff b^+(j) b^-(j) <= 0.  OPEN sub-case: coarse
      in-window free coordinates touched by targets of carriers c > l with b^+(j) b^-(j) > 0 (excluded if targets of carriers lie in F u K,
      as for V4's l_-).

## 4.4 What is (and is not) obtained.  Labels.
 (1) PROVED: Lemma S, Corollaries S1, S2, Proposition S3, Theorem NL, Proposition FZ (Parts 1-2); Lemma A; properties (b)-(e) of
     Theorem NT, Proposition NT-M, the dead-zone bump (Part 3); Lemma QB2, Lemma VT (single stage), Lemma R-pin (this part);
     Proposition RT*(a),(b),(d).
 (2) PROVED modulo refereed results: Corollary FZ (Master Theorem III'), Corollary NT-R (V4 Theorem 5.6; design compatibility of V4's
     conditions with D^{V2} assumed, V4-ref F6).
 (3) SKETCH: existence part of Theorem NT; recovery of all mates of f^infty (Part 3.4); Proposition RT*(c),(e); the general form of
     (S1); (S2a), (S2b), (S2d) of 4.3'.  HEURISTIC: (S2c).  PROVED (new): Lemma VT at a single stage (4.2).
 (4) OPEN (precise): (S1) in general (multi-block coupling with value-dependent coefficients, V2's (C*-3)), and the uniform composition
     (S2) = (S2a)-(S2d) of 4.3'.  Assuming them,
     every F-finite (C*) row is in Rec for D^{V2} (with V4's design conditions), i.e. Lemma Z holds for F finite.
 (5) NOT a gap any more (relative to V2-ref's list): (C*-1) exact absorption of fine-peak residues — replaced by quadratic banks (finitely
     many coordinates) + violation tolerance (tail), no Slater condition needed; (C*-2) (SC) at companions — holds along gap scales below
     the donor raise for aligned re-alignments; (C*-4) scale-dependent shift directions — the exact combinatorial cone of (a) contains
     every direction used at the scales of w up to O(K t) (Hoffman projection inside a FIXED cone at the companion), and fine-level
     incoherence for a direction different from the completed ray is a fine-origin violation; (C*-5) joint completion/absorption —
     no completion (Lemma C5) is needed once fine violations are tolerated.  These claims are SKETCH-level (they rest on (S2)).

## 4.4' Lemma R-pin (pinned strict non-peaks bound the shift from above).  PROVED (any admissible T, any f, scale t <= min(t_eta, 1)).
For every block m and every strict non-peak k in Q_m with w_m(k) != 0, the decompositions of Lemma lem:twosided satisfy
     Delta d_m |w_m(k)| <= 3 gap_m(k)/t + |Delta Theta_m(k)|      (decomposition convention Delta d = d_+ - d_-).
Proof.  Lemma lem:suplevel(f) with varsigma := sgn w_m(k): varsigma omega_+(k) <= (1 - d_+ t) gap/t and varsigma omega_-(k) >= -(1 + d_- t)
gap/t; with |d_+- t| <= 1/2 this gives varsigma (omega_+ - omega_-)(k) <= 3 gap/t.  Since Theta_+- = omega_+- - d_+- w,
omega_+ - omega_- = Delta Theta + Delta d w, so varsigma(omega_+ - omega_-)(k) = varsigma Delta Theta(k) + Delta d |w(k)|.  QED
Consequences.  (i) A class-R strict non-peak (|Delta theta_k| = lambda_k |Delta Theta(k)| <= K_g t, Y1 Lemma 3.1) with gap <= t^2 pins the
upward shift: Delta d |w(k)| <= 3 t + K_g t/lambda_k — it is an UPPER source not listed among Y1's (U1)-(U3) (adding it only enlarges case
(I)).  (ii) [configuration (i), upward shift Delta d^{dec} > 0] In the transplant of 4.3(c), a coarse class-R strict non-peak k of a
shifted block is an omega-carrier with net coefficient 0 (Dom(k) = Delta^{data} w(k)); by the lemma either the shift is O(K t) at the scale
t (then the d-neutral machinery of V1/V2 applies) or |Dom(k)| ~ |Delta d^{dec}||w(k)| <= 3 gap/t + K_g t/lambda_k, which is within the
size conditions of Z3 Lemma U up to a constant factor.  [Configuration (ii) (downward shift): the lemma gives no bound; there the
neutralizing moves are inward (away from the peak level) and are covered by Z3 Lemma 5.1 / Y2 Lemma U'(ii) — SKETCH.]

## 4.5 Remarks on scepticism.
 (a) Lemma QB2's quadratic cost is the key quantitative fact: a violation of mass epsilon costs a companion move of order
     epsilon^2/beta, so fine-origin violations of mass <= T_lo^3 cost o(T_lo^6) — far below the o(T_lo^2) allowed by Theorem E.  Coarse
     violations of size O(K t) (budget errors) would cost K^2 T_hi^2 >> T_lo^2 and are NOT tolerable: coarse exactness (Proposition
     RT*(a) and (S1)) is indispensable.  This matches the structure of all previous rounds (exact data on coarse coordinates).
 (b) Theorem NL shows that the choice of approximants is essential; every approximant used above is ALIGNED (V4's hysteretic
     re-alignment, banks of the contact's own sign), as Proposition S3 requires.
 (c) Finite SOCP models cannot exhibit failure of recovery (finite truncations are block-tame); they confirm Proposition S3 / Theorem NL
     (collapse of the oscillating part of the fibre under a far anti-type flip: max oscillation 0.0160 -> 2.4e-8 while p*(f_n - f) = 8.3e-7)
     and the quadratic bank law of Lemma QB2.
