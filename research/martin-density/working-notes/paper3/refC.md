# Referee report C on `paper3/martin_density_note_III.tex`: Section 5 (infinite base support: truncation and transport)

**Scope.** Section 5 (`sec:III-inf`), lines 4592-6909 of `paper3/martin_density_note_III.tex` (7093 lines, build of 2026-10-11 04:33):
- 5.1 truncation (Lemma ctrunc, Lemma LT, Remark LTsharp, Corollary LTwin);
- 5.2 the engineered approximant at arbitrary support (Lemma ballinf, Definitions windowinf, approxinf, levsys, Theorems UEinf and Eenginf);
- 5.3 cushion domination (Lemmas nocubeinf, deepraise, track, nodeep, Proposition cushion, Lemma noBinf);
- 5.4 levers and preparation (Definition resources, Lemmas identity, actions, offset, driftid, Definition prep, Lemma prep);
- 5.5 the d-consistency system (Lemma leftDC, Theorem SysDC, Lemma tol);
- 5.6 Step A (Definitions SysA, Areg, Lemmas Euler, cone, border, Theorem Aobs, Corollary Asuff);
- 5.7 the design T^infty_fin (Definition designinf, Lemmas designinf, depthclean, late, costs, bookkeeping);
- 5.8 transport (Definition H1, Lemma H1suff, Theorem transport, Corollary transport, Remark LR);
- 5.9 residual (Definition residual, Proposition residual, Remarks residual, infdep).

**Sources (authoritative where they conflict with the paper).**
- r10: Q2_notes.md (with Q2_part1-4), Q2_referee_a.md, Q2_refa_notes.md (A.1, A.2, B.1, B.2, C.1-C.7).
- r11: K1_notes.md, K1_referee.md, K1_ref_notes.md (R-1 ... R-14, E); K2_notes.md, K2_referee.md, K2_ref_notes.md (W-1, K-1 ... K-8, P-3, P-4, B-G).
- Certification reports: r11/cert0_report.md (Step 0 of KN^tr, alternative C3), cert2_report.md (E^eng, subset version, P6), cert3_report.md (base dependence).
- Cross-checks against the paper's own Sections 2-4:
  - Lemma ball, Lemma masses, Lemma DC, Definitions window and approx, Lemma UE1, Theorem UE, Proposition S2c;
  - Proposition KNtr (l.1498-1500);
  - Lemma nocube (l.4259-4271);
  - Remark later (Section 6, l.7011-7030).
- Part I (paper/martin_density_note.tex: lem:peakshift, def:recovery) and Part II (paper2: lem:II-cost, lem:II-DR, prop:II-LSC).
- Label numbers against paper3/labI.txt and labII.txt.

The r12 files (J1, J2) are not authoritative here. I used J2_notes 1.3 and Proposition J2.4 only as a cross-check of a sign computation that I re-derived myself from [I, Lemma 8.27] (R12).

**Coordination.** Referee B (refB.md R9, R19, R20) raised three items that touch Section 5:
- the notation c_1;
- the base of T^infty_fin in Remark infdep;
- the sign of the data at weak peaks in Lemma H1suff(i).

They appear below as R10, R16 and R12. The Section-5 parts are stated completely here, so the two reports agree.

## 0. Verdict

**The analytic core of Section 5 is correct and faithful to the refereed sources.** I re-derived:
- Lemma ctrunc, Lemma LT (including the partial form and the four-case identity), Remark LTsharp and Corollary LTwin;
- the modifications (M0)-(M5) of Theorem UEinf, including the 32-rho constants and the 1 - 1.28 delta budget;
- the whole averaging proof of Theorem Eenginf;
- Lemmas track and nodeep, and the deep assignment of Proposition cushion;
- Lemma identity, Lemma actions and Lemma driftid;
- Theorem SysDC, Steps 1-6;
- Lemmas cone (a), (b) and border, Theorem Aobs (1)-(6) and Corollary Asuff (a)-(f).

**Incorporated fixes.** Every fix of the referees and the certification listed below is in the paper, except where a required fix says otherwise:
- Q2-refa: p1.1, p2.1, p2.5 / B.1, and C.3, which is superseded;
- K1-ref: R-3, R-6, R-7 (bypassed by Theorem SysDC), R-8 and R-13 (the descriptions by carrier types are necessary conditions only). R-1 is only partly incorporated (R5) and R-4 is not (R4);
- K2-ref: W-1, K-1-K-8, P-3 and P-4;
- cert2: subset averaging and P6.

**Overclaiming.**
- Section 5 never claims (LSC-trunc) for every f, nor density.
  - l.4629-4630 says explicitly that neither is proved here.
  - Proposition residual and Remark residual (a) are stated as necessary conditions only.
- Heuristic and sketch material is labelled: Remark trunc-heur, Remark cube, Remark Asuff (c) and Remark residual (d).
- **One overclaim remains.** Remark infdep asserts that Master Theorem VI holds for T^infty_fin, by a monotonicity argument that does not cover the change of base (R16).

**Required fixes: 16** (R1-R16). None of them changes the conclusion of the transport theorem under its stated hypotheses.

Several of them are more than cosmetic:
- **R1:** Theorem UEinf, as stated for an arbitrary truncation tolerance theta_tr, is not covered by its proof.
- **R7:** the cushion proposition does not state (U3^inf) on the whole support of the companion, and its C_+ = 5 contradicts the C_+ = max(5, C_f) used everywhere else.
- **R11:** Section 5's Step 0 pushes weak peaks, while the route-V companion of the paper (Proposition KNtr) explicitly does not. The pushes are needed in Section 5, but this is nowhere said or justified.
- **R12:** Lemma H1suff(i) is false as stated, for three reasons:
  - the sign of the data at weak peaks;
  - the orientation of pulls and banks;
  - the depth of the pulls.
- **R13:** Lemma H1suff(ii) applies a rank-one argument to shared moves, where the system is not rank one.
- **R15:** Proposition residual has a quantifier slip.
- **R16:** the overclaim in Remark infdep.

**Optional suggestions:** 16 (O1-O16).

| # | Lines | Item | Kind |
|---|---|---|---|
| R1 | 4856-4864, 4941-4946, 4979-4990 | theta_tr arbitrary: f' may leave B_f; nu'-clause of Lemma UE1(c) | gap in statement/proof |
| R2 | 4968-4969, 5293-5294 | Lemma masses(ii) cited for infinitely many mass coordinates | citation outside hypotheses |
| R3 | 5148-5153 | Remark reduction(a): truncated rows and hypothesis (a) | false as written |
| R4 | 5218-5220 | Lemma nocubeinf: error Kt should be K_data t | K1-ref fix not incorporated |
| R5 | 5272-5275, 5296-5299 | Lemma deepraise(c): moduli are rate objects and scale by 1/lambda_r | K1-ref R-1 not fully incorporated |
| R6 | 5277-5283, 6560-6561, 6756-6757 | theta_w: "theta_w >= T" vs "theta_w may be chosen <= T" | inconsistent; needed for (E-e) |
| R7 | 4612-4614, 5445-5474, 5521-5523, 5795-5800, 6715-6722 | (U3^inf) on all of supp a^#; C_+; normalization | incomplete / inconsistent |
| R8 | 5789-5794 | Lemma prep(a), (b): the closing moves (P_1) | bounds false as stated |
| R9 | 5676-5677, 5702, 5708, 6611-6613 | val_l = eps_l u_l: "eps_l val_l", "vs_k val_k" | sign slips |
| R10 | 6224-6325, 6802-6851 | c_1 used for the Step-A constant | notation clash (refB R9) |
| R11 | 6606-6613, 6707-6713, 6495 | Step 0 pushes vs. Proposition KNtr (no push) | cross-section inconsistency |
| R12 | 6611-6613, 6615-6626, 6637-6662, 6776-6783 | Lemma H1suff(i): data sign, orientation, depth | false as stated (refB R20) |
| R13 | 6643-6646, 6656-6661 | Lemma H1suff(ii) with shared moves | proof does not apply |
| R14 | 6624-6625 | Definition H1: "Equivalently ... A-regular" | not equivalent |
| R15 | 6799-6821 | Definition / Proposition residual | quantifier slip |
| R16 | 4599-4602, 5167-5170, 6892-6907 | Master Theorem VI for T^infty_fin; base change mu to mu^* | overclaim (refB R19) |

## 1. Required fixes

### R1. Theorem UEinf and Definition approxinf(ii): an arbitrary truncation tolerance theta_tr is not covered by the proof (l.4856-4864, 4941-4946, 4979-4990).

**Quote, Definition approxinf(ii):** "$\|U^*a_01_{(N_w,\infty)}\|\le s_1T^4,\qquad \alpha_0(N_w):=\sum_{j\in F_0,\,j>N_w}|a_0(j)|\le\theta_{\rm tr}$, for a prescribed $\theta_{\rm tr}>0$".

**Quote, Theorem UEinf:** "Then for every choice of $N_w$, $N''$ as in Definition~\ref{def:III-approxinf} the approximant $f'$ is norm attaining, ...".

**Problem.**
- (a) **f' need not lie in B_f.** The proof keeps "everything not mentioned" verbatim from Theorem UE.
  - The step "Consequences of (LATE)" of Theorem UE derives p*(f'-f) <= r_f and concludes "f' lies in B_f, and Lemma ball holds at f'".
  - Step 4 uses the transfer vectors of f' (Lemma ball(b)), and Lemma ballinf requires p*(f''-f) <= r_f(eta_1).
  - With truncation, the bound available is p*(f'-f) <= r_f/2 + K_w(Pi log(e/Pi) + s_1) + 2(1+||U||)^2 alpha_0(N_w).
  - (LATE) controls the middle term. Nothing controls the last term when theta_tr is not small, so f' need not lie in B_f.
- (b) **The nu-clause of Lemma UE1(c) fails.** (M2) asserts that the truncation "enters only through value and e moves". But it also changes nu.
  - a' = A(P*)/q*(A(P*)) with q*(A(P*)) ~ 1 - alpha_0(N_w), so nu' ~ nu_0/(1 - alpha_0(N_w)).
  - Hence |nu' - nu_0| <= K_w Pi fails unless alpha_0(N_w) <~ Pi.
  - Only the lower bound nu' >= nu_0 - K_w Pi is used downstream: in Lemma UE1(f), and in the relative error of [I, Lemma 3.3] in Step 3. It does hold: truncation lowers q* by about alpha_0(N_w) and changes ||U* .|| by at most s_1 T^4 <= Pi. But the proof must say so.
- Q2 2.3 had alpha_0(N_w) <= theta T^2/(1+||U||) with theta -> 0. The paper replaced it by an arbitrary theta_tr.

**Change.** In Definition approxinf(ii), require
  alpha_0(N_w) <= theta_tr <= min( s_1 T^4 , r_f(eta_1)/(8(1+||U||)^2) ).
- Then the truncation changes q* by at most 2 s_1 T^4 <= Pi.
- Every clause of Lemma UE1 then holds verbatim, with K_w enlarged by an f-constant, and f' lies in B_f by (LATE).

In the proof of Theorem Eenginf, "Choose $N_{w,j}$ with $\alpha_{0,j}(N_{w,j})$ so small that (E-e) holds" is then compatible.

*Alternative:* keep theta_tr <= r_f(eta_1)/(8(1+||U||)^2) and add to (M2): "Lemma UE1(c) holds with |nu' - nu_0| <= K_w Pi replaced by nu' >= nu_0 - K_w Pi (truncation lowers q* and changes ||U* .|| by at most s_1 T^4); this is the only form used in Lemma UE1(f) and in Step 3."

### R2. Lemma masses(ii) is cited outside its hypotheses (l.4968-4969, 5293-5294).

**Quotes.**
- (M2): "By Lemma~\ref{lem:III-masses}(ii), truncating $a_0$ beyond $N_w$ moves $e$ by at most $\Pi_{\rm tr}$".
- Proof of Lemma deepraise(b): "$\|e^r-e\|\le2\|U^*\Delta a\|/\nu$ (Lemma~\ref{lem:III-masses}(ii))".

**Problem.** Lemma masses (l.1745-1777) is stated for A = a + sum_{s in J} c_s e_s^* with J FINITE. The truncated tail F_0 ∩ (N_w, infinity) and the raise set R(J) are infinite in general.

**Change.** Cite the elementary inequality ||x/||x|| - y/||y|| || <= 2||x - y||/||y||, valid for all nonzero x, y. It is the one used in the proof of Lemma ctrunc(b).
- Write "by Lemma ctrunc(b) applied at f_0" in (M2).
- Write "by the inequality in the proof of Lemma ctrunc(b)" in the proof of Lemma deepraise.
- Alternatively, drop "J finite" from Lemma masses(ii); its first assertion does not use it.

### R3. Remark reduction(a): truncated rows and hypothesis (a) (l.5148-5153).

**Quote:** "and truncated rows (Lemma~\ref{lem:III-LT}) with $\lambda_j=1$ and $\varepsilon'_j=2\max_r\Lambda(r)+\varepsilon''_M$ at the finitely many scales of Corollary~\ref{cor:III-LTwin}."

**Problem.**
- Hypothesis (a) of Theorem Eenginf is required for ALL r. A bound "at the finitely many scales" is not (a).
- Remark LTsharp(b) (Q2-refa A.2) shows that the cushion loss cannot be controlled uniformly in r by anything better than alpha(M).
- What is true: since Lambda_M(r, B) <= alpha(M) for every r, Lemma LT(a), applied to an optimal decomposition of f + r rho g (dual ball), gives
    p*(f^M + r rho g) <= s(rho r) + 2 alpha(M) + eps''_M   for all r.

**Change to:** "truncated rows f^M (Lemma LT) satisfy (a) for all r with lambda_j = 1 and eps'_j = 2 alpha(M) + eps''_M, since Lambda_M <= alpha(M). The bound 2 max Lambda_M + eps''_M + eta r^2 holds only at the finitely many scales of Corollary LTwin (Remark LTsharp(b))."

### R4. Lemma nocubeinf: the Gamma_w error is K_data t, not K t (l.5218-5220).

**Quote:** "with the $\Gamma_w$-bound improved to $\Gamma^\#_w(b^-,\omega^-)^{1/2}\le\Gamma^\#_w(B_-,\Theta_-)^{1/2}+Kt$".

**Problem.**
- Here K is the projection constant C_f(Des/u)^C (l.5326).
- The minus side differs from the decomposition's minus side by the projection error and by the class-zeroing error.
- The zeroing error is A_{i(t)} K t, with A_i = K_*(w)^i <= K_*(w)^{J+1}.
- K1-ref (verdict table, Lemma K1.1: "Gamma error is K_data t (notation)"; R-4) and Section 4's own Lemma nocube (l.4270) both have K_data t.

**Change:** "+Kt" to "+K_data t", with K_data as in Proposition cushion.

### R5. Lemma deepraise(c): the moduli are rate objects and do not move by M_f(L)||U* Delta a|| (l.5272-5275; proof l.5296-5299).

**Quote:** "every value $u_k(\zh)$ moves by at most $2\|U^*\Delta a\|/\nu$, and every rate object of level $L$ by at most $M_f(L)\|U^*\Delta a\|$ \textup{(}[II,~Lemma~6.45]\textup{)}."

**Problem.**
- The moduli |a_s|, s <= dbar(L), are rate objects: (I3), l.6437-6438, used at l.5312.
- Item (c) itself says they are divided by lambda_r. So they change by |a_s|(1 - 1/lambda_r), which can be as large as 2 psi_L(J) |a_s|. This is not <= M_f(L) mu*_J psi_L(J).
- [II, Lemma 6.45] (paper2 l.10136-10154) makes exactly this distinction:
  - (O1), (O2), (O6), (O11) are unchanged;
  - (O10), the support moduli, are divided by lambda_r;
  - only (O3)-(O5), (O7), (O8), (O12) move by M_f(l)||U* Delta a||.
- This is K1-ref R-1. It is incorporated only in the first clause of (c).
- The tiny/robust conclusion stated after the lemma is correct.

**Change the clause to:** "the rooms (and (O1), (O2), (O6), (O11) of [II, Lemma 6.45]) are unchanged; the support moduli ((O10) and the moduli |a_s| of (I3)) are divided by lambda_r in [1, 1 + 2 psi_L(J)]; the minors and cofactor polynomials of the enlarged class cones (I3) depend only on design data and on the pattern, which is unchanged; every other rate object of level L moves by at most M_f(L)||U* Delta a||."

In the proof, add that tiny moduli stay <= b and robust ones stay >= u/2, because lambda_r <= 2.

### R6. The sequence theta_w: incompatible requirements (l.5279-5283, 6560-6561, 6756-6757).

**Quotes.**
- Lemma deepraise: "where $\theta_w\to0$ is a prescribed sequence with $\theta_w\ge T$".
- Proof of Lemma costs: "(a) gives $\theta_w/(c_fu)^2\to0$ since $\theta_w$ may be chosen $\le T$ and $u\ge T^{1/20}$".
- Transport, Step 8: "$\theta_j:=\theta_w+\theta'_w+e^{-1/(3T)}T^{-2}$ satisfies $\theta_j/c_{\rm flat}(w)^2\to0$".

**Problem.**
- With only "theta_w -> 0, theta_w >= T", the ratio theta_w/c_flat(w)^2 >= theta_w/u(w)^2 need not tend to 0, since u(w) -> 0 along main stages.
- So (E-e) of Theorem Eenginf (theta_j/c_flat(j)^2 -> 0; K1-ref R-6) is not established.
- The proof of Lemma costs silently chooses theta_w <= T. Together with theta_w >= T, this forces theta_w = T.

**Change.** In Lemma deepraise set theta_w := T. Then:
- the first condition reads C_f mu*_J log(e/mu*_J) <= T^3;
- the J(w) bound is unchanged, since log_2(1/(theta_w T^2)) = 3 log_2(1/T);
- theta_w/(c_f u)^2 <= T^{9/10}/c_f^2 -> 0.

In the proof of Lemma costs, replace "may be chosen $\le T$" by "$=T$".

### R7. Proposition cushion: (U3^inf) must hold on all of supp a^#, and the constant and the normalization must agree with Lemma prep(c) (l.4612-4614, 5445-5474, 5521-5523, 5795-5800, 6715-6722).

**Quotes.**
- Proposition cushion (l.5467-5468): "so \textup{(U3$^{\inf}$)} holds on $F$ with $C_+=5$ and excess $r(j):=|V_f(j)|+\mathrm{tr}_j$".
- Lemma prep(c) (l.5795-5798): "$b^+=\chi V'+\beta_s$, $b^-=-(1-\chi)V'+\beta_s$ ... $|\beta_s|\le C_ft\theta_0$; hence \textup{(U3$^{\inf}$)} holds there with $C_+=\max(5,C_f)$". Its proof (l.5828-5829) has "$\beta_s=-\varkappa a^\#_s/a^\#(\zh^\#)$ and $|\varkappa|\le C_ft$".
- Transport, Step 5 (l.6718-6722): "with cushion constant $C_+=\max(5,C_f)$ ... At companion support coordinates outside $F$ the data are those of contacts of the bank's sign, which satisfy (U3$^{\inf}$) with the base term only."
- Introduction (l.4612-4614): "are cushion dominated with an absolute constant (Proposition~\ref{prop:III-cushion})".

**Problems.**
- (a) **Uncovered support coordinates.** Definition windowinf requires (U3^inf) at every j in F_0 = supp a_0, here supp a^#. But supp a^# is strictly larger than F. It contains:
  - the banks of (P_2);
  - the base banks of the TU pre-placements of Step A;
  - the PULLED coordinates off F. These are the pre-placed TU pulls, and the Step-0 pulls at pullable far contacts j not in F, which carry mass of sign -eps_l.

  Proposition cushion proves (U3^inf) only on F. Its item (ii) covers only pulls in F (F_low ⊂ F). Lemma prep(c) and Step 5 cover banks. Nothing covers pulled coordinates off F, and Step 5's sentence ("contacts of the bank's sign") is not true there.
  - The bound needed at such a coordinate is the one proved in (iii) of the proof for F_low:
      t|b^±(j)| <= t|V(j)| <= 24 lambda_l v_l(j) = |a^#_j|   for t <= T_hi(w),
    as in V1 TR(iv). Its proof does not use j ∈ F.
- (b) **Two normalizations and two constants.**
  - Proposition cushion corrects the base term with -varkappa a^#_Z/a^#_Z(zhat^#), where |varkappa| <= K t and a^#_Z(zhat^#) >= 1/4. At a bank s not in Z this gives |beta_s| <= 4K t|a^#_s| <= |a^#_s|/t, because 4K t^2 <= 1. So C_+ = 1 there.
  - Lemma prep(c) uses another normalization, a^#(zhat^#) with |varkappa| <= C_f t, and concludes C_+ = max(5, C_f). This is the constant of K2-ref C.1.
  - Step 5 and Lemma bookkeeping use max(5, C_f), while the introduction calls the constant absolute.

**Change.**
- Add to Proposition cushion:
  - "(iv) at banked coordinates s in supp a^# \ F (banks of (P_2) and TU base banks): b^± are contact-like of sign z_s up to the fine residue, plus the base term -varkappa a^#_s/a^#_Z(zhat^#) of modulus <= 4Kt|a^#_s| <= |a^#_s|/t (Lemma prep(c));"
  - "(v) at pulled coordinates j in supp a^# \ F: t|b^±(j)| <= |a^#_j|, as in (ii)."
- State the conclusion as "(U3^inf) holds on supp a^# with C_+ := 5 and excess r(j)".
- Make Lemma prep(c), Step 5 and Lemma bookkeeping use the same normalization (a^#_Z, |varkappa| <= K t) and the same constant.
- If C_+ = max(5, C_f) is kept instead, replace "an absolute constant" (l.4614) by "a constant depending only on $f$".

### R8. Lemma prep(a), (b): the bounds ignore the closing moves (P_1) (l.5789-5794).

**Quotes.**
- (a): "$p^*(f^P-f^r)\le C\bar d(L)\theta_0\log(1/\theta_0)+C_fp^*(L^*(w^P-w^r))$, and this is at most $C\bar d(L)b\log(1/b)/\mathrm{Des}(L)^{C_P-1}$."
- (b): "Every value moves by at most $C\bar d(L)\theta_0\le b$".

**Problem.**
- (P_1) closes up to dbar(L) tiny rooms. These are z-moves of size up to b.
- They move values by up to b||u_k||_1 <= b. The proof of (b) says this itself ("the closing moves change each value by at most $b\|u_k\|_1\le b$ in total"), which contradicts the statement of (b), since theta_0 = b/Des^{C_P} << b.
- For (a): by [II, Lemma 2.12(iv)], the normer change of these z-moves costs C_f c(delta) with value moves of order b. That is up to C_f(|Lambda_L| + dbar(L)) b log(1/b), not C dbar b log(1/b)/Des^{C_P-1}.
- The later uses survive. Lemma costs(b) already uses C dbar(L) b log(1/b) = o(u^2 T^2). K2-ref F checked that a doubled b suffices for the clean dichotomy.

**Change.**
- (a): "$p^*(f^P-f^r)\le C_f\mathrm{Des}(L)\,b\log(1/b)$".
- (b): "Every value moves by at most $b+C\bar d(L)\theta_0\le2b$ (closing moves $\le b$, banks and raises $\le C\bar d(L)\theta_0$), every rate object by at most $2\,\mathrm{Lip}\cdot b$".

### R9. Sign slips with val_l = eps_l u_l (l.5676-5677, 5702, 5708, 6611-6613).

**Quotes.**
- Definition resources (l.5600): "$\mathrm{val}_l:=\epsilon_lu_l(\hat x_1)$".
- Lemma actions (l.5675-5677): "normalized so that a unit step changes $\epsilon_l\mathrm{val}_l$ privately by $1$, every coarse $k$ satisfies $\mathrm d(\epsilon_k\mathrm{val}_k)=(\delta_{kl}-g_kh_l)\,\mathrm dP$".
- l.5702: "(P2) shifts $\epsilon_l\mathrm{val}_l$ down".
- l.5708: "$z$-moves there lower $\epsilon_l\mathrm{val}_l$ only".
- l.6611-6613: "The push must lower $\mathrm{vs}_k\mathrm{val}_k$ ... a near bank (which raises $\epsilon_k\mathrm{val}_k$)".

**Problem.**
- Since val_l already contains eps_l, eps_l val_l = u_l(xhat).
- Re-derivation from Lemma actions(i). Put dP := eps_l ((mu*_s)^2/nu) v_l(s) dm. A mass change dm at the thick s ∈ N_l changes:
  - u_k(xhat) by -<U* u_k, e> h_l dP, for k ≠ l (since u_k(s) = 0);
  - u_l(xhat) by eps_l dP - <U* u_l, e> h_l dP.
- Hence d val_k = (delta_kl - g_k h_l) dP. The displayed formula is wrong by the factor eps_k.
- Likewise:
  - pulls and far z-moves lower val_l;
  - a near bank raises val_k;
  - the inward push of a weak peak must lower vs_k u_k(xhat) = vs_k eps_k val_k.
- K2 has the same slip; K2-ref E corrected only "(H1)'s eps_k val_k".

**Change.**
- In l.5676, 5677, 5702 and 5708, replace "$\epsilon_l\mathrm{val}_l$" and "$\epsilon_k\mathrm{val}_k$" by "$\mathrm{val}_l$" and "$\mathrm{val}_k$".
- In l.6611-6613, write "lower $\mathrm{vs}_ku_k(\hat x)$" and "(which raises $\mathrm{val}_k$)". For the sign of eps_k at weak peaks, see R12.

### R10. Notation: c_1 is used for the Step-A constant (l.6224, 6252, 6295, 6313-6325, 6802, 6810, 6836, 6851).

**Quote (l.6224):** "$c_1:=1/(2+CN|\Lambda_A|^{1/2}/A_{\min})$".

**Problem.** In this paper, c_1 is the weight of stage 1, which equals ||T_fin|| under option (a) (l.195, 3238-3239). Section 5 itself works with T^infty_fin, option (a).

**Change.** Rename the Step-A constant to $c_{\rm A}$ at all the listed lines. This is the same change as refB R9, which also covers the introduction.

### R11. Step 0: Section 5 pushes the active weak peaks, while the paper's route-V companion does not (l.6606-6613, 6707-6713, 6495).

**Quote (l.6606-6610):** "Step~0 of the route-V companion pushes every active weak peak $k$ of a (T)-block ($\varrho_k\in[1,1+b]$) to $\varrho_k\le1-b$ before the \L ojasiewicz step, so that it becomes a strict non-peak; this is needed for the threshold protection of Section~\ref{sec:III-routeV} and for the smallness of the non-peak Euler share used in Theorem~\ref{thm:III-Aobs}."

**Compare with the proof of Proposition KNtr (l.1498-1500):** "\emph{Step 0 (closing moves).}  Apply only the closing moves (C1), (C2) of the assembly ...; there is no donor raise in active blocks, and the active weak peaks are \emph{not} pushed at this stage." See also Remark K1 (l.644-655), the floor convention.

**Problems.**
- (i) **Misdescription.** The paper's route-V companion (Proposition KNtr, used in Section 4) follows cert0's alternative C3: no weak-peak push; the active weak peaks enter the pattern's Omega under the floor convention. Its threshold protection is proved without pushes. So the quoted sentence misdescribes the route-V companion, and "needed for the threshold protection" is wrong.
- (ii) **The real reasons are not stated.** Section 5 does need the pushes, but for its own reasons:
  - **Lemma cone(c)** computes the block scalars with the coarse peak set frozen at f_1 + P (K2-ref K-8). It then declares the frozen statuses consistent because rho_d <= 1 - mu/2 for the near-threshold active carriers. That is consistent only if those carriers are strict non-peaks at f_1 + P. An unpushed active weak peak would be frozen as a peak and end as a non-peak.
  - **Theorem Aobs** uses |Xtilde_m| <= 1/4. This needs every tuned carrier to be a strict non-peak of f_1: the derivative of varkappa_m in a peak coordinate is of order one (cf. "$d\kappa/d\zeta(c)\ge3/4$" for peaks, K2 5.4(g)).
- (iii) **Mismatched variant.** Transport Step 4 invokes "the Step-A conclusions of Section routeV" (Lojasiewicz/Puiseux targets, threshold protection). But its companion has a different Step 0 from the one for which Steps 1-3 of Proposition KNtr are proved in the paper.

**Change.** Replace the paragraph at l.6606-6613 by an explicit statement:

"At arbitrary base support we use the variant of Step 0 in which, after the closing moves, every active weak peak of a (T)-block is pushed to $\varrho\le1-b$ by moves of total size $\le\mathrm{Des}(L)^Cb/u$ (condition (H1$^*$) below). Steps 1-3 of the proof of Proposition KNtr hold for this variant: at $f_1$ one has $P\supseteq P_{\rm rob}$ and $\Omega\subseteq Q$, so Lemma F gives $F_\Phi(r_1)\le1+C_*b$ (cert0 3.1), and the radius of (D1) is enlarged by (I5). The pushes are needed here, and not in Proposition KNtr, because Lemma cone(c) freezes the coarse statuses and Theorem Aobs uses the non-peak Euler share."

- Delete "needed for the threshold protection of Section~\ref{sec:III-routeV}".
- Let Step 4 of the transport proof and Lemma depthclean refer to this variant.

### R12. Lemma H1suff(i) is false as stated: the data sign at weak peaks, the orientation of pulls and banks, and the depth of the pulls (l.6611-6613, 6615-6626, 6637-6662, 6776-6783).

**Quotes.**
- l.6611-6613: "the peak carries data of sign $\epsilon_k=-\sgn(\Delta''_m)\mathrm{vs}_k$, so a near bank (which raises $\epsilon_k\mathrm{val}_k$) performs the push only if $\Delta''_m>0$."
- Lemma H1suff(i) (l.6640-6642): "every active weak peak of a (T)-block has a \emph{private} push resource: a pullable far coordinate at depth in $[2b\bar\vartheta_m\Phi_k/m,x'_{\max}]$, a near bank with $\Delta''_m>0$, or (P3);"
- Its proof (l.6650-6656): "Private pushes of size $\le2b\bar\vartheta\Phi_k/m$ change the values of the other carriers only at second order ...; so pushing each peak to $\varrho\le1-2b$ realizes Step~0. Overshoot is harmless ..."
- Proof of Corollary transport (l.6782-6783): "and every active weak peak has a private far pull, which is Lemma~\ref{lem:III-H1suff}(i)."

**Problems.**
- (a) **The data sign at a weak peak is wrong in the subcase 0 < Delta'_m < e_k.**
  - At an active weak peak k the route-V data are gamma_k = lambda_k(Delta omega(k) - Delta_m w(k)), with w(k) = M vs_k and Delta'_m = Delta_m M.
  - [I, Lemma 8.27] (lem:peakshift) gives varsigma_k omega_+(k) <= 0 <= varsigma_k omega_-(k). Hence vs_k Delta omega(k) = e_k := |omega_+(k)| + |omega_-(k)| >= 0.
  - So vs_k gamma_k = lambda_k(e_k - Delta'_m), that is, eps_k = vs_k sgn(e_k - Delta'_m).
  - The formula -sgn(Delta''_m) vs_k is the one for robust peaks, where Delta omega = 0. It fails when 0 < Delta'_m < e_k.
  - I re-derived this. The same computation is in r12/J2_notes 1.3. The paper records it in Remark later(a) (l.7011-7030) but leaves the lemma unchanged; refB R20 makes the same point.
- (b) **Orientation.** A far pull at a contact of sign eps_k lowers val_k = eps_k u_k by 2 v_k(j). A near bank raises val_k. The inward push must lower vs_k u_k = vs_k eps_k val_k. Hence:
  - a far pull pushes inward iff eps_k = vs_k (e_k > Delta'_m);
  - a near bank pushes inward iff eps_k = -vs_k (e_k < Delta'_m);
  - if e_k = Delta'_m, the peak carries no data and the composite move (P1) is available.

  Lemma H1suff(i) lists the far pull with no orientation condition. It is therefore false whenever a weak peak with eps_k = -vs_k has only a far pull (that pull pushes outward). It also lists the bank under the wrong condition Delta''_m > 0.
- (c) **Depth.**
  - Definition H1 requires push moves of "total size at most $\mathrm{Des}(L)^Cb/u(w)$". This keeps the Lojasiewicz start inside the radius of (D1), as modified by (I5), and it is what Lemma depthclean (l.6495-6496) uses.
  - A pull at depth v moves the value by 2v. Lemma H1suff(i) allows v up to x'_max = u^2 T^3/(Des^2|Lambda|), which is in general far larger than Des^C b/u (b <= T^4, and typically much smaller).
  - The proof treats only "private pushes of size <= 2 b thetabar Phi_k/m". A pull at depth v >= 2 b thetabar Phi_k/m has size 2v > 2 b thetabar Phi_k/m.
  - "Overshoot is harmless" is not justified beyond the (D1) radius. The pushed peak enters R^2 = m^2 sum r_l^2 of Lemma K, so an overshoot v moves floor statuses and tiny minors at r_1 by O(v).

**Change.**
- Replace (i) by: "every active weak peak $k$ of a (T)-block has a private push resource of the correct orientation:
  - if $\epsilon_k=\mathrm{vs}_k$ (i.e. $e_k>\Delta'_m$, [I, Lemma 8.27]), a pullable far coordinate $j\in S_k$ with $v_k(j)\in[2b\bar\vartheta_m\Phi_k/m,\ \mathrm{Des}(L)^Cb/u(w)]$;
  - if $\epsilon_k=-\mathrm{vs}_k$ ($e_k<\Delta'_m$), a near bank;
  - if $e_k=\Delta'_m$, the composite move (P1);
  - or (P3)."
- Correct l.6611-6613 accordingly (together with R9).
- In Definition H1, replace "near banks of peaks with $\Delta''_m>0$" by "near banks of weak peaks with $\epsilon_k=-\mathrm{vs}_k$", and the pull window by $[2b\bar\vartheta_m\Phi_k/m,\mathrm{Des}(L)^Cb/u(w)]$.
- In the proof of (i), use pushes of size <= Des^C b/u, and note that the pull mass 24 lambda_k v_k(j) acts on other values only through e, with efficiency (mu*_j)^2, which is negligible for j > s_max(L).
- In the proof of Corollary transport (l.6782-6783), write: "every active weak peak has a private push of the right orientation:
  - a far pull if $\epsilon_k=\mathrm{vs}_k$. Its far coordinates are contacts of sign $\epsilon_k$. Since consecutive elements of $S_k$ have $v$-ratio $2^{-2^{k+1}}\ge\mathrm{Des}(L)^{-1}$, the smallest one with $v_k(j)\ge2b\bar\vartheta\Phi_k/m$ satisfies $v_k(j)\le\mathrm{Des}(L)\,2b\bar\vartheta\Phi_k/m$;
  - a near bank if $\epsilon_k=-\mathrm{vs}_k$. Its near coordinates are contacts of sign $\epsilon_k$;
  - (P1) if it carries no data."
- Remark later(a) can then become a pointer.

### R13. Lemma H1suff(ii): the rank-one argument does not apply to shared moves (l.6643-6646, 6656-6661).

**Quotes.**
- (ii): "the active weak peaks $W$ that are pushed by (P4) or by shared design-depth moves satisfy $|1-h_W^Tg_W|\ge u$".
- Proof: "The rows of $W$ form the system $I-g_Wh_W^T$ up to second-order terms; by the Sherman--Morrison formula ...".

**Problem.**
- The form I - g_W h_W^T is right for (P4) pushes at distinct private thick near coordinates: the column is e_k - h_k g (Lemma actions).
- A shared design-depth move acts at a coordinate s that lies in the supports of several weak peaks. Its column has first-order private entries eff_s c_s(u_{k'}) for every k' with u_{k'}(s) ≠ 0 (Lemma actions (i)-(iii)). K2-ref E names exactly these "first-order private effects u_{k'}(s) on other weak peaks at shared coordinates".
- So for such moves h_W is not defined, the row system is not rank one, and the Sherman–Morrison bound does not apply.
- The "private push resources" of the other peaks are also subject to R12.

**Change.**
- Restrict the scalar condition |1 - h_W^T g_W| >= u to peaks pushed by (P4) at distinct private thick near coordinates.
- For shared design-depth moves, require instead: "the matrix of first-order actions of the chosen moves on the rows of $W$ (private and common-mode parts) has a right inverse of norm $\le\mathrm{Des}(L)^C/u(w)$".
- The rest of the proof is unchanged: the rows of W are solved with moves <= Des^C b/u, and the private pushes, oriented as in R12, absorb the first-order cross effects.

### R14. Definition H1: "Equivalently ... A-regular" is not an equivalence (l.6624-6625).

**Quote:** "Equivalently, the Step-0 inequality system, with the needed decreases as right-hand side, is A-regular in the sense of Definition~\ref{def:III-Areg}."

**Problem.**
- A-regularity (Definition Areg) is a robust condition, B(b, rho_0) ⊂ (W/2)Q, for a system of equations, with W = Des^{C_A} u^{-3} max(x, ||b||) built on the Step-A scale x.
- (H1*) asks for admissible moves of total size <= Des^C b/u that solve INEQUALITIES (overshoot allowed).
- A-regularity of the Step-0 system, with W and rho_0 taken at the Step-0 scale, implies (H1*) by the Brouwer argument of Lemma cone(c). The converse fails: a feasible inequality system need not contain a ball of radius rho_0 around its right-hand side.
- With the W of Definition Areg, the moves may exceed Des^C b/u.
- K2-ref E has the same "equivalently".

**Change to:** "In particular, (H1$^*$) holds if the Step-0 system, with the needed decreases as right-hand side, is A-regular in the sense of Definition~\ref{def:III-Areg} with $x$ replaced by $2b$ and $W\le\mathrm{Des}(L)^Cb/u(w)$ (Brouwer argument of Lemma~\ref{lem:III-cone}(c), statuses frozen)."

### R15. Definition and Proposition residual: quantifier slip (l.6799-6821).

**Quotes.**
- (A*): "(H1$^*$) holds, and for every pre-placement $\mathcal P$ there is a near-certificate $y$ ... with $\varphi_y>-\rho_0$ and $\gamma\le-\gamma_0$".
- (U*): the same, with "$-\gamma_0<\gamma\le-c_1\nu_1/(8H(L))$".
- Proposition residual: "... at every clean sub-window $w$ of $L$ and every class $a$ ..., \textup{(W$^*$)}, \textup{(A$^*$)} or \textup{(U$^*$)} holds."

**Problem.**
- The proof shows: either (H1*) fails, or for every P there is a near-certificate y_P with phi > -rho_0 and gamma(y_P) <= -c_*.
- Which of the two types y_P has may depend on P. So "(A*) or (U*)", each of which demands one fixed type for EVERY P, does not follow.
- K2-ref G states the residual as one combined alternative, (A*)/(U*).

**Change.** Merge the two conditions into one:

"(A$^*$/U$^*$) (H1$^*$) holds, and for every pre-placement $\mathcal P$ there is a near-certificate $y$ of size $<4u^3\mathrm{Des}(L)^{-C_A}$ with $\varphi_y>-\rho_0$; it is of \emph{type} (A$^*$) if $\gamma\le-\gamma_0$ and of type (U$^*$) if $-\gamma_0<\gamma\le-c_{\rm A}\nu_1/(8H(L))$."

Then state Proposition residual (ii) per certificate.

The same change applies to:
- item (4) of the opening of Section 5 (l.4624-4627: "one of the conditions (W$^*$), (A$^*$), (U$^*$)");
- the introduction (l.286-304) and the residual list of Section 6. Coordinate these with refB.

### R16. Master Theorem VI for T^infty_fin: the change of base is not covered (l.4599-4602, 5167-5170, 6892-6907).

**Quotes.**
- Remark infdep (l.6900-6903): "Theorem~\ref{thm:III-MTVI} holds for $T^\infty_{\rm fin}$ as well, because its proof uses the design only through conditions that are monotone under the insertions (Lemma~\ref{lem:III-designinf}(d))."
- l.5167-5170: "From now on the operator is the design of Section~\ref{sec:III-design} over the doubly exponential diagonal base $\mu^\star_s:=2^{-2^{2^s}}$, enlarged as in Definition~\ref{def:III-designinf} below (all enlargements only increase $\mathrm{Des}(L)$ and the rate scheme, ...)".
- l.4599-4602: "For the design of Section~\ref{sec:III-design} with option (a) the first half is Theorem~\ref{thm:III-MTVI}; so for that design density for $p_N$ is equivalent to \textup{(LSC-trunc)}$_N$.  This section treats \textup{(LSC-trunc)}."

**Problem.**
- T^infty_fin differs from T_fin not only by the insertions (I1)-(I5) but also by its base: mu*_s = 2^{-2^{2^s}} instead of mu_s = 2^{-s^2-1} (Remark twodesigns, l.6993-7009). Lemma designinf(d) covers the insertions only.
- Master Theorem VI was certified for the base mu. cert3 Section 4 re-derived the mu-base Lemma TU / bank efficiency ("the only refereed source ... for T_fin's base"); (B3), (W2), (W6) of Lemma interface were also checked for mu. So the stated reason does not prove "Theorem MTVI holds for T^infty_fin".
- The same transfer underlies Theorem transport itself. It uses the route-V companion of Section 4 (Proposition KNtr, Lemma CMtr, the status lemma) and the window count for T^infty_fin.
  - Q2, K1 and K2 assumed this through the base-independence of the window theorems (U2 Remark after 1.1; U4 Lemma GW; K1_notes 1.0: "Every window theorem uses the base only through B_mu*").
  - It was not re-verified for T_fin's own recursion over mu*.
- The opening paragraph combines "for that design" (T_fin) with results that are proved for T^infty_fin.

**Change.**
- (i) In Remark infdep, replace the quoted sentence by:

  "We expect Theorem~\ref{thm:III-MTVI} to hold for $T^\infty_{\rm fin}$. The insertions are covered by Lemma~\ref{lem:III-designinf}(d). The change of base $\mu\to\mu^\star$ enters Section~\ref{sec:III-MTVI} only through (B3), (W2), (W6) of Lemma~\ref{lem:III-interface} and the tuning lemma behind Proposition~\ref{prop:III-transfer}; each has a $\mu^\star$-analogue in Part~II, but this transfer has not been written out or verified."

  Make the following sentence conditional: "if, in addition, Theorem~\ref{thm:III-MTVI} holds for $T^\infty_{\rm fin}$, then ...".
- (ii) In the first sentence of Remark infdep, state that the results of Sections 2-4 are used for T^infty_fin through the base-independence of the window theorems ([II, Lemma 3.22]; the base enters only through the bank factor in Des), and that this was not re-verified line by line.
- (iii) After l.4602, add: "From Subsection~\ref{subsec:III-cushion} on, the operator is $T^\infty_{\rm fin}$ (Definition~\ref{def:III-designinf}); for it the first half of the equivalence is expected but not verified (Remark~\ref{rem:III-infdep})."
- This matches refB R19.

## 2. Optional suggestions

- **O1. Lemma LT(b) (l.4689-4692).** Add the hypothesis a + Delta a ≠ 0, since f[A,z] is defined only for A ≠ 0.
- **O2. Remark LTsharp(a) (l.4739-4744).**
  - The display attains the factor 2 only up to the terms 2 mu*_j Lambda_M and 2||U* a_{>M}|| <= 2 mu*_{M+1} alpha(M).
  - Say in what sense the factor "cannot be lowered". For example: j = M+1 along a subsequence with mu*_{M+1} alpha(M) = o(|a_{M+1}|); this is automatic unless |a_j| decays doubly exponentially.
- **O3. Theorem Eenginf, (E-e) and (E-f) (l.5073-5083).**
  - Both involve N_{w,j} (through Pi_j, tail_{W,j} and alpha_{0,j}), while the proof chooses N_{w,j}.
  - State them with N_w-free quantities and let the proof choose N_w:
    - (E-f'): K_w(K_w s_1 + c_fine) < K_j T'^2;
    - (E-e'): eps'_j + K_w(K_w s_1 log(e/(K_w s_1)) + s_1) < theta_j T'^2.
  - This uses that Pi log(e/Pi) is increasing on (0,1].
- **O4. Theorem UEinf (l.4937-4941) and transport, Step 7 (l.6731-6733).**
  - (W-a) of Theorem UE contains K_J; say K_J := K_lev.
  - Hypothesis (i) of Proposition S2c contains "(W-b) holds". (W-b) is a condition on Lemma DC, which Section 5 replaces by (DC) of the lever system. Say so in Step 7.
- **O5. Remark drift (l.5753-5770).** "exact $d$-consistency with those levers is impossible" is proved in Q2-refa C.5 under specific hypotheses:
  - no absorbers;
  - h^T p_m = 0 in every block;
  - u_h = varkappa a_0 on F_0;
  - c_alpha = 0.

  State them and cite the source.
- **O6. Theorem SysDC (ii) (l.5893-5895).** At a ZD coordinate that carries mass (banked by (P_2), or raised), use the mass-change column of an S_th coordinate, not the composite move. K2-ref B.2 notes that the two branches of the composite move differ by Des(L) m at a coordinate of mass m.
- **O7. Proofs of Lemma cone(a) (l.6144-6146) and Lemma costs (l.6563-6564).** "$T\le(u/(4\,\mathrm{Des}(L)))^{20}$" gives only a fixed power, while C_A, C_1 and the exponents "Des^C" are unspecified. Cite instead T = 2^{-n(w)} T_hi(w) with n(w) >= Q(w) >= (4 Des(L)/u)^{20}, which beats every fixed power of Des/u for L large.
- **O8. Proof of Lemma deepraise (l.5300-5306).** J(w) > s_t(L), so the bound on 2^{J(w)} also needs 2^{s_t(L)+1} <= Des(L). Say that this follows from the factor B*(L) = 2^{s_t(L)}/(delta_min (mu*_{s_t})^2) of Des(L) in Part II, or put s_t(L) into (I2).
- **O9. Proof of Lemma bookkeeping (l.6599).** The computation as written gives |S| c_flat/K_data >= c_f (n(w) Q(w))^{1/4}, not c_f n(w)^{1/2}. The limit infinity is unaffected.
- **O10. Proposition residual (i) (l.6827-6831) and Remark residual (c) (l.6872-6875).**
  - Write "approximately proportional (error $\varepsilon\mathrm{Des}(L)/|\varkappa_\Psi|$)".
  - Specify the row. The a_s are the moduli at f_1 + P: those of f at design depth divided by lambda_r, up to the Step-0 and preparation moves.
  - Compare refB R10 for the introduction.
- **O11. Lemma track (l.5340-5363).** The proof treats Omega carriers and coarse peaks of relative margin >= u/2 only. Add one sentence on weak peaks:
  - active weak peaks belong to the pattern's Omega;
  - for an inactive weak peak, e_k <= A_i K t by inactivity, so the peak case applies with this error.

  This makes "for every coarse carrier $l$" fully covered.
- **O12. Definition levsys (DC) (l.4899-4900), with Theorem SysDC Step 6 and Lemma late (L4).** Say that r_0 is chosen with C_2 K_DC^2 r_0 <= 1/4, the condition used in the Poincare–Miranda step.
- **O13. Opening item (1) (l.4604).** "Truncating the base support costs nothing at finitely many scales": write "is asymptotically free at finitely many scales fixed beforehand (its cost $2\Lambda_M+\varepsilon''_M$ tends to $0$)".
- **O14. Proof of Lemma nodeep (S) (l.5403-5404).** "$v_l(j)=\delta_l2^{-j}/n_l$" is stated only beyond s_max(L) (l.5181), but it is used for j < J(w), j ∉ T(L), which may lie below s_max(L). Say that it holds on all of S_l.
- **O15. Corollary transport (second claim).** Cite its sources: Q2 Corollary 5.2 (a sketch there) and K1 Corollary K1.C(b), proved after K1-ref R-12. Note that it uses both the far pull and the near bank of every weak peak, depending on the orientation (R12).
- **O16. Remark later(a) (Section 6).** After R12 is applied, replace the remark by a pointer to the corrected Lemma H1suff(i). A remark labelled "not verified and not used" should not contradict a stated lemma.

## 3. Verification log (what was checked and found correct)

### 5.1
- **Lemma ctrunc.** (a)-(d) re-derived. (d) uses that mu* is non-increasing (Q2-refa p1.1). (c) goes through [I, Prop 1.12] (ii)=>(i), which is valid without norm attainment.
- **Lemma LT.** Both parts re-derived, including the identity |s alpha + x| - |x| = alpha - 2 min(alpha, y) (three cases) and the partial form min(|Delta a|, (y - alpha')_+).
- **Remark LTsharp.** (a) and (b) re-derived; (b) is Q2-refa A.2.
- **Corollary LTwin.** Correct.
- **Remark trunc-heur.** Labelled heuristic.
- **Label references.** [I, Prop 1.9, 1.11, 1.12; Lemmas 1.6, 1.7, 7.1(b), 7.4, 7.5] and [II, Lemmas 2.12(iv), 2.15; Cor 2.17; Prop 6.48] resolve to the intended statements.

### 5.2
- **Lemma ballinf.** Matches Q2 2.1.
- **Definition windowinf.** (U3^inf) with residues r_i(j) generalizes Q2 2.2. The residues are paid in (M3)(1) at cost <= 2 rho|tau| r_i(j), which is counted in eps_i.
- **Theorem UEinf, (M0)-(M5).** Re-derived; R1 and R2 are needed. In particular:
  - the order s_1 -> N_w;
  - r <= K_w s_1 and K_lev|F(0)| <= r/4;
  - Pi_X <= 128 rho s_1 mu*_1 n A_0/(T nu_0);
  - the four new coordinate classes;
  - the bracket 1 - 2 delta + (0.71875) delta <= 1 - delta;
  - the constants 32: W_F and 1/(32 rho C_+) are consistent with (PR beta)'s |A(P)(j)| >= |A_1(j)|/4;
  - the cost term 2(1+||U||)^2 alpha_0. This is cruder than Q2's but valid.
- **Theorem Eenginf.** Proof re-derived line by line:
  - both cases;
  - the dyadic count over a subset of scales (cert2);
  - [I, Lemma 3.6(a)] and [II, Cor 2.17];
  - window-dependent C_{+,j} and c_flat(j) (Q2-refa B.1 / p2.5).

### 5.3
- **Lemma track.** K1.2 with K1-ref R-3: K_*(w) >= 6(H(C_Gamma J + 1) + 1), relative to |c_l|.
- **Lemma nodeep.** K1.3; cases (D), (T), (S), (O) re-derived. The constant C_q = (8/3)(4/q_0 + 8) accounts for q_0^r >= q_0/2.
- **Proposition cushion (i)-(iii).** Deep assignment with trace slack re-derived. The Z-treatment (b^±(j) = ± V/2, base term on a^#_Z) keeps b^theta = 0 at ZD lever coordinates; it is a correct refinement of K1.A. See R7 for the missing coordinates.
- **Lemma noBinf.** K1.S, correct.
- **Remark cube.** Labelled heuristic (K1.1').

### 5.4
- **Lemma identity.** K2.2 and K2.3, with the signed dichotomy of K2-ref B.1.
- **Lemma actions.** K2.4, with the composite-branch sign corrected per K2-ref B.2; see R9 for the val notation.
- **Lemma offset.** K1 (C2), confirmed by K1-ref.
- **Lemma driftid.** Q2 Lemma 3.4, re-derived.
- **Definition prep and Lemma prep(c), (d).** K2 4.1 and K2-ref C.1.

### 5.5
- **Lemma leftDC.** (c) is exact with the paper's G_m.
- **Theorem SysDC, Steps 1-6.** Re-derived, with P-3 (cut-off beyond N'') and P-4 (|Omega|^{1/2}, the number of rows) incorporated.
- **Remark SysDC.** "Bypassed, not absent", per K2-ref C.3.
- **Lemma tol.** K2.1, with (u1)-(u4) and the mis-bound re-derived.

### 5.6
- **Lemma Euler.** K2.8.
- **Lemma cone.** (a) and (b) re-derived. K-7 (u^3 scaling) and K-8 (frozen statuses) incorporated.
- **Lemma border.** Both cases and the near-null claim re-derived.
- **Theorem Aobs.** (1)-(6) re-derived, with K-1 (|kappa| m_k in (2a)), K-2 (v_k > 0 on S_k) and K-3 (2|kappa| b) incorporated.
- **Corollary Asuff.** (a)-(f); the general bordered scalar (1 - Xtilde)lambda_c h^T rt + h_c h^T gtilde is correct.
- **Remark Asuff.** (g) is moved to a remark as a reduction (K-4). The "Moreover" of K2 5.5 is dropped (K-5). (c) is labelled a sketch.

### 5.7
- **Definition designinf (I1)-(I5).** Equal to (K2-a)-(K2-e) together with K1-ref R-8(ii).
- **Lemma designinf.** K2.12.
- **Lemma depthclean.** K2.13.
- **Lemma late.** K2.14; (L1) is consistent with the constant 32 of W_F.
- **Lemma costs.** K2 6.5 and K1-ref R-6 (x'_max).
- **Lemma bookkeeping.** K1.B with C_+ = max(5, C_f), and (E-d).

### 5.8
- **Theorem transport.** Matches K2-ref G: (H1*) per W-1, K-7, K-8, the order of choices, and Step 8's verification of (a) and (E-c)-(E-f). Subject to R1, R6, R7, R11 and R16. Definition H1, Lemma H1suff and Corollary transport are subject to R12-R14.
- **Remark LR.** (LR) => (H2), per K-7.

### 5.9
- **Proposition residual.** A necessary condition only, as K-6 requires; subject to R15.
- **Remark residual.** (a), (b) and (e) are accurate; (d) is labelled heuristic.

### Overclaiming
- Neither (LSC-trunc)_N for every f nor density is claimed (l.4629-4630, Remark residual (a), the last clause of Remark infdep).
- Every statement concerns the designed operator T^infty_fin.
- The only overclaim is the sentence on Master Theorem VI for T^infty_fin (R16).
