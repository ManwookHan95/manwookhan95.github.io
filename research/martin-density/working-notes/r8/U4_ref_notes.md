# U4 referee notes (Round 8): proofs of the precisions and of the independent re-derivations

Part files: r8/U4_ref_part1.md (T_final, Lemma W, Theorems 2.2, 2.3), U4_ref_part2.md (conflicts C1-C9, numerics for C1),
U4_ref_part3.md (Lemma GW, dependency tables, VP', MT III', N-dependence), U4_ref_part4.md (master theorem, status flags).
Scripts: r8/U4_ref_work/tu_mu_hp.py (+ .out), rr_check2.py (+ .out).  Notation: paper/martin_density_note.tex ("the note"), U4_notes.md.
Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  No counterexample is claimed or suggested.

## 0. Summary
Every claim U4 labels PROVED is correct.  The two new defects U4 found in the literal union of the Round-7 designs are real and its fixes
are right: C1 (the bank factor of V1's Design must be calibrated to the base: B_mu(l) = 2^{sigma(l)}/mu_{sigma(l)}^2) and C7 ((GM) at
l = 1 forces c_1 < 1).  I found eleven precisions (q1)-(q11), none of which changes a statement of the master theorem or the
definition of T_final in substance.  New evidence: a 3000-bit test of V1 Lemma TU with the ACTUAL base mu_s = 2^{-s^2-1} and banks at
j' = 8 ... 14 shows the admissible tuning size is governed by mu_{j'}^2 v(j')^2 uniformly over 270 binary orders of magnitude, i.e.
by exactly the quantity B_mu(l) controls (U4's own script did not reach the super-exponential regime).

## 1. Precisions (each PROVED; proofs below)
(q1) Order of stage l.  V4-ref R6 lists "delta_l by (GM)" before "y_l by allowedness (a)", but the (GM) intervals
     {delta : |sum_j sigma_j y_l(j) + eps delta H_l| < g_l} depend on y_l and g_l depends on |supp y_l|.  T_final's order
     (target, then delta_l, then c_l) is the only consistent reading; it is what U4 uses.
(q2) (SF*) second half and (GM) are imposed for l >= 2 only; (SF*) second half has no meaning at l = 1 (no c_0), so only (GM) is a
     genuine restriction (C7).
(q3) C1, "the literal factor can fail": an explicit instance (Section 2).
(q4) C1(v), "the mu-base is FORCED": what is forced is super-exponential decay of the base entries; any such base gives (RR) for every
     power profile (Section 3); "(RR) fails" means "Theorem RS does not apply", not "the row is not recovered".
(q5) C7: V4 Lemma 3.4's threshold "l > log_2(2 Theta) + 1 >= 2" needs Theta >= 1; since Theta is any upper bound of theta_m one may
     replace it by max(Theta, 1), and all uses of Lemma 3.4 concern carriers beyond an f-dependent level.
(q6) Status flags: the purely double-refereed version of Theorem RS is V3's original statement with V3's non-degeneracy (ND_B)
     (Lambda : l_1(F) -> R^B onto, which implies (ND'_B)), (RR_{U_B}) and (H3'); the (ND') fix and L_0 = B_np are single-referee.
(q7) U4 1.3(5) states sigma(l) <= s_max(l) + 2^{l+1}; this is false when s_max(l) < 2^l (e.g. s_max = 9, l = 10: min S_10 = 3072 >
     2057).  Correct bound: sigma(l) <= max(3*2^l, s_max(l) + 2^{l+1}).  The bound is used nowhere.
(q8) U4 Theorem 2.2(d) writes "eta(w) <= T_lo(w)^4 <= 2^{-4l^3} < 1/Design(l)"; the middle inequality is false (Design(l) >= 2^{6 l^3}).
     Correct chain: eta(w) = T_lo(w)^4/(l Design(l)) < 1/Design(l) <= 1/C_L(l) (T_lo < 1, C_L >= 1 a factor of Design).  Also the final
     clause "Design^k T_lo(w) <= u(w)/8 for k <= 4 and l large" holds for every l: T_lo(w) <= 2^{-Q(w)} <= Q(w)^{-2} <= (u/(4 Design))^{40}.
(q9) Master Theorem (iii), (E1) gloss "|a_s| below a power of mu_s": HEURISTIC; failure of (RR) forces infinitely many active s with
     |a_s| < y U(s) and mu_s U(s) not much smaller than y^{1+eps}, i.e. roughly |a_s| <~ mu_s^{1-o(1)} U(s).
(q10) U4's numerics tu_mu_check.py use s_j = 2^{-beta j^2}, beta in [0.002, 0.006], banks at j' ~ 11-13: s'^2 in [0.25, 0.7]; they do
     not test the super-exponential regime.  Replaced by tu_mu_hp.py (Section 4).
(q11) Theorem 2.3's "every design feature used by the refereed results of Rounds 5-7" must read "... by the refereed results on the
     three dependency trees and by V4's positive results": the explosive-window results (Z3-ref part 4) and V4 Lemma 2.6 (lacunary) use
     features T_final deliberately lacks (U4 C5 says so; the theorem statement should too).

## 2. (q3): an admissible instance where V1's literal factor 8^{sigma} fails for the mu-base.  PROVED.
Claim.  There are data (D0_final) (a dense target family and a schedule) such that for infinitely many levels l every bank
coordinate s' of level l (s' = min(S_c ∩ (s_max(l), inf)), c <= l) satisfies mu_{s'}^2 v_c(s') < Design_V1(l)^{-1/6}, where
Design_V1 is V1's literal Design(l) (8^{sigma(l)} in place of B_mu(l)) evaluated for the base mu.
Proof.  Take any dense sequence in c_00 ∩ S_{q^*} and interleave, at a sparse set of indices i in I_*, PURE targets
y^(i) := e_{s_i}^*/q^*(e_{s_i}^*) with s_i odd, to be chosen when i is scheduled for the first time (stage l_i); the family stays dense.
The recursion up to stage l_i - 1 does not involve s_i.  At stage l_i, y_{l_i} = e_{s_i}^*/(1 + mu_{s_i}) with s_i larger than every
coordinate used so far:
 - (GM): for sigma = +-1 the excluded deltas are near 1/((1 + mu_{s_i}) H) >> delta^max; for sigma = 0 only delta < g/H is excluded;
   so delta_{l_i} = delta^max_{l_i} whatever s_i is.  g_{l_i} = delta^max H/96 (|supp| = 1).
 - c_{l_i} = min (W1)-(W7): (W4) is empty (s_i is odd), (W5), (W6), (W7), (W1)-(W3) do not involve s_i: c_{l_i} is independent of s_i.
 - n_{l_i} in [3/4, 5/4] and delta°_{l_i} = delta H/n vary with s_i only through mu_{s_i}, within fixed bounds; Lambda°(l_i), D(l_i)
   (m^nat removes T(l) ∩ S_{l''}, which does not contain s_i) and Xi^Y are bounded by constants independent of s_i.
 - In every cone/configuration system of level l_i the column of the carrier l_i has exactly one non-zero entry, u_{l_i}(s_i) =
   1/((1 + mu_{s_i}) n_{l_i}) in [1/2, 2], in the row of the fresh coordinate s_i, and that row has no other non-zero entry (s_i is in
   no other coarse support, and coarse targets avoid S_{l_i} by allowedness (a)).  Every such system is the direct sum of the
   s_i-independent system of the other carriers and a 1 x 1 system; its Hoffman constants, extreme rays and the pseudo-inverse
   norms of H_tune are bounded independently of s_i; so are G^*, H_comb, G^**, H_tune and |T(l_i)|.
Hence Design_V1(l_i)^{1/6} <= A_i 2^{s_max(l_i) + 3 sigma(l_i)} <= A_i 2^{4 s_i + 3*2^{l_i+1}} with A_i independent of s_i, while every
bank coordinate of level l_i exceeds s_max(l_i) = s_i, so mu_{s'}^2 v_c(s') <= 2^{-2 s_i^2 - 2 - s_i}.  Choosing s_i with
2^{2 s_i^2 + 2 + s_i} > A_i 2^{4 s_i + 3*2^{l_i+1}} gives the claim at every l_i, i in I_* (infinitely many levels).  QED
Remark (why the defect needs fast targets).  sigma(l) >= min S_l = 3*2^l, and 1/c_l grows like a tower of height l (c_{l+1} <= b(l,M(l))^2
<= 2^{-8 n(w)}, n(w) >= Q(w) >= Design(l)^{20} >= c_l^{-120}); D(l) >= 1/Phi_l >= 1/c_l is a factor of Design_V1(l), so Design_V1(l) already
dominates 2^{12 sigma(l)^2} whenever s_max(l) is below (roughly) the square root of log_2(1/c_l).  The defect bites only for target
supports growing faster than the design tower; B_mu(l) costs nothing and removes it.  (A perturbative instance — adding eps e_{s_i}^* to a
general target — would need a genericity argument, because Hoffman constants are not upper semicontinuous in the entries, which move
with mu_{s_i}; the pure fresh targets avoid this.)

## 3. (q4): what (RR) requires of the base.  PROVED.
Setting: W = v_l on S_l (gaps G_l = 2^{l+1}), W_s = (delta_l/n_l) 2^{-s}; |a_s| = 2^{-(1+b)s} on S_l (b > 0); base entries beta_s
decreasing.  Active set at y = 2^{-L}: {s in S_l : 2^{-bs} < y} = {s > L/b}.  M^W(y) = sum_{s in S_l, s > L/b} beta_s W_s.
(a) beta_s = 2^{-s}: M^W(y) is comparable to 2^{-2L/b} = y^{2/b} (geometric tail with ratio 2^{-2 G_l}); (RR) (M = O(y^{1+eps}) for
some eps > 0) holds iff 2/b > 1, i.e. b < 2.
(b) If beta_s <= 2^{-phi(s)} with phi(s)/s -> infinity (super-exponential decay), then M^W(y) <= C 2^{-phi(L/b) - L/b}, and
phi(L/b) >= K L for every K once L is large: (RR) holds for every b > 0 and every eps.  mu_s = 2^{-s^2-1} (phi(s) = s^2 + 1) and
2^{-s^{3/2}} are examples.
(c) Conversely, if (RR) is to hold for every b > 0 for these profiles, then for every K, beta_s 2^{-s} <= C_K 2^{-K s} along S_l, i.e.
beta_s decays faster than every exponential along S_l.
Numerics (rr_check2.py): exponents log M/log y at y = 2^{-100}, 2^{-200}, 2^{-400}: base 2^{-s}: 4.01, 2.01, 1.01, 0.67 (b = 0.5, 1, 2,
3; limit 2/b); base 2^{-s^{3/2}}: 58.8, 21.2, 7.7, 4.2 (growing with L); base mu: 1610, 405, 103, 45.
Hence "the mu-base is forced" should read "a super-exponentially decaying diagonal base is forced (for RS to cover power-law support
swallowing with b >= 2); mu_s = 2^{-s^2-1} is the choice of V3".  Rows violating (RR) may still be recovered by other results
(e.g. Y3 Theorem 3.5 under its hypotheses).

## 4. C1 in the super-exponential regime: high-precision numerics (evidence only)
tu_mu_hp.py (mpmath, 3000 bits): V1 Lemma TU (pulls of mass 24 lambda v(j) at v(j) in [eta, 2^G eta], private banks at j' = min S_l,
explicit scalar fixed point y = Phi(y), m_l(y) = (Delta_l y + beta_l (y - nu_p))/(mu_{j'}^2 v')) with the ACTUAL base mu_s = 2^{-s^2-1},
banks at j' in {8, 10, 12, 14} (mu_{j'}^2 = 2^{-130} ... 2^{-394}), 1-3 tuned carriers, pull coordinates up to ~460, eta = fac x reg,
reg := min_l mu_{j'}^2 v_l(j')^2.
 - fac <= 0.1: 36/36 converge; val^# - val^(2) = x to working precision; bank masses > 0 and ~ eta/(mu'^2 v'); |Phi'| <= 0.09, with
   |Phi'| reg/eta in [2e-4, 3]; other carriers move by (0.01 ... 122) eta^2/reg.
 - fac = 1: 8/12 converge (one with a negative bank mass); fac = 10: 4/12; fac = 100: 0/12.
The threshold sits at eta ~ reg for every j' (270 binary orders of magnitude of reg): Lemma TU's c_T must contain the bank factor
mu_{j'}^2 v'^2, which B_mu(l) bounds below by (4/5)^2 delta_min^2 2^{-sigma}/B_mu >= Design(l)^{-1/3}.  Consistent with C1 and with
V1-ref (p4) (contraction constant ~ 1/(s'^2 v'^2)).

## 5. Independent re-derivations recorded (details in the part files)
- Theorem 2.2: (T-a)-(T-d), Lemma B conclusion, (P1)-(P3) per sub-window, V2's (2.1) (part 1).
- Lemma W: dependency trace of every quantity of stage l; no forward reference; N-freedom (part 1).
- C1: every base-dependent inequality of V1 3.1-3.4 / V2 Theorem B with B_mu (part 2, 2.1(a)-(d)).
- C7: H_1 = 1/60, delta^max_1 = 1/2, c_1 <= 2^{m(1)+k(1)}/240 (part 2).
- Lemma GW against thm:R0, Prop. TR / Theorem E'' / MT II, RS' Step 1 (part 3); GW also absorbs C_f^{omega(l)}.
- VP' under (ND') (part 3, 3.3), including lam >= 1 and the extra RT error 2||Delta a''||_1.
- MT III' logic: tau' <= tau_0 is never used after V1's Step 3; Sigma^# contains every row V1's Steps 4-5 use (part 3, 3.4).
- N-dependence: (2A_max)^{-N} >= 1 sits in the lower bound of the nonzero minors (part 3, 3.5).
- Master Theorem (i)-(iv) as an assembly; constant-sign maximal contact; martintail conditional form (part 4).
