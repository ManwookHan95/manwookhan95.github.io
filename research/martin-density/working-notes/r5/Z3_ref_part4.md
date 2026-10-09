# Z3 referee, part 4 — the band is a design artifact: explosive windows (new; PROVED unless marked)

Z3 4.3(ii)/7.1 claim that a carrier whose room lies in the band theta T_lo(l_*)^2 << r_l << 1/K_*(l_*) defeats the window method, that
"every design has band carriers for suitable f" and "no choice of design removes it". The first claim (per window) is right; the
design-independence is FALSE. The point: with the SLD window lengths n^w_l ~ l 2^{l^3} Lambda°(l), the bands of consecutive windows
overlap enormously (lower end ~4^{-n^w_l}, upper end ~2^{-l^{2.5}/N}), so ONE carrier blocks ~l^{1.6} consecutive windows and a sequence
of carriers can block all of them. If instead the window-length function grows explosively, the bands become pairwise disjoint, each
carrier blocks at most one window, and since there are far fewer carriers of p_N below L than window indices below L (blocks m > N
also index windows), infinitely many windows are band-free for EVERY f.

## 4.1 The explosive variant (D1^F) of Definition def:SLD.
Keep (D0), allowedness, y_l, n_l, u_l, delta°_l, Lambda°(l) and (D2) unchanged. Replace the factor l 2^{l^3} by a design function F(l):
   n^w_l := ceil(F(l) Lambda°(l)),  T_hi(l) := min{T_lo(l-1), 1/(F(l) Lambda°(l))},  T_lo(l) := 2^{-n^w_l} T_hi(l),
   c_{l+1} := min{c_l/4, T_lo(l)^3},
with F(1) := 2 and, recursively (all quantities on the right are fixed at stage l),
   F(l+1) := max{ F(l)^2, (l+1) 2^{(l+1)^3}, b(l)^{-4(l+1)} },
   b(l) := 4^{-2 n^w_l} T_hi(l)^4 delta_min(l) 2^{-s_max(l)} / l,   u(l) := F(l)^{-1/(4l)},
where delta_min(l) := min_{l'' <= l} delta_{l''} and s_max(l) := max of the union of supp y_{l''}, l'' <= l (finite sets; s_max := 1 if empty).

Lemma 4.1.1 (survival). PROVED. Theorem thm:SLD holds for (D1^F), with (P3) replaced by (P3^F): T_hi(l) F(l) Lambda°(l) <= 1,
n^w_l >= F(l) Lambda°(l), T_hi(l+1) <= T_lo(l). Every result of Section 8 of the note, and every result of Z3 parts 1-6, holds for
(D1^F) after replacing l 2^{l^3} by F(l) in (W+-), (W*), (W*_pk) and in the window-growth conditions.
Proof. The admissibility proof uses only (D0), allowedness (a),(b), c_{l+1} <= c_l/4 and delta_l, n_l; (P1), (P2) are unchanged. In all
recovery proofs (Theorems thm:R0, thm:Bstar, thm:Bpm, thm:S, Z3 Theorems 5.3, 5.4, Corollary 3.4) the window factor enters only through
T_hi(l) * Q_f(l) Lambda°(l) -> 0 and n^w_l / (Q_f(l) Lambda°(l)) -> infinity for f-dependent factors Q_f(l) <= C_f^{l^2} (e.g.
varpi_0^{-l^2}, (3/(2 gamma))^l), or through the (W)-conditions themselves; F(l) >= l 2^{l^3} >= C^{l^2} eventually gives both. The box
bound sum_{l > l_*}|Delta theta_l| <= 6 t^2 uses only c_{l_*+1} <= T_lo(l_*)^3, kept. QED

Lemma 4.1.2 (disjoint bands). PROVED. u is nonincreasing, b(l) < u(l), and u(l') <= b(l) for all l < l'. Hence the open intervals
Band(l) := (b(l), u(l)) are pairwise disjoint.
Proof. u(l+1) = F(l+1)^{-1/(4(l+1))} <= F(l)^{-2/(4(l+1))} <= F(l)^{-1/(4l)} = u(l) (as 2l >= l + 1), and u(l+1) <= b(l) by the third term
of F(l+1). b(l) <= 4^{-2n^w_l} <= 4^{-2F(l)} < F(l)^{-1/(4l)} = u(l). For l < l': u(l') <= u(l+1) <= b(l). QED

## 4.2 Band-free windows exist for every first row.
Proposition 4.2.1. PROVED. Let (D1^F) be as above, N >= 1, and let (rho_l)_{l in L_N} be any numbers in [0, infinity] (in the
application rho_l := r_l/delta°_l, a property of f). Call a window index l_* BLOCKED if some l in L_N with l <= l_* has
rho_l in Band(l_*). Then at most |L_N cap [1,L]| indices in [1,L] are blocked; hence infinitely many indices are not blocked.
Proof. By Lemma 4.1.2 each rho_l lies in at most one Band(l_*), so choosing for each blocked l_* <= L one blocking carrier l <= l_*
defines an injective map into L_N cap [1,L]. The number of unblocked indices in [1,L] is therefore >= |[1,L] \ L_N|, which tends to
infinity because N \ L_N = {l : m(l) > N} is infinite (frak j is a bijection of N x N and N is finite). QED
(For the original design this fails: under the conditions (G1) gaps of L_N are O(l^{1/2}) and (G2) delta°_l >= 2^{-l^2}, the rooms
r_l = 2^{-l^4} delta°_l, l in L_N, block every window; see part 2, 2.7.)

## 4.3 What an unblocked window gives.
Proposition 4.3.1. PROVED (conditional). Let f in S_{p*} have F finite, a finite exactly swallowed set B, and sign-mixed rooms r_l > 0 for
l in L_N \ B; put rho_l := r_l/delta°_l. Let l_* >= l_0(f) be unblocked, and let
   E := {l in L_N cap [1,l_*] \ B : rho_l <= b(l_*)},   P := {l in L_N cap [1,l_*] \ B : rho_l >= u(l_*)}
(so the coarse carriers are B u E u P), let eps_l (l in E) be the sign minimizing sum v_l(s)(1 - eps z_s), and let f^# be the coarse
exactification of f with A := E (Z3 part 3). Then:
 (a) K_* := (1/q_0 + 22) Lambda*_{f,B'}(l_*), B' := E u B, satisfies K_* <= C_f^{l_*} F(l_*)^{1/4} Lambda°(l_*), PROVIDED
     (S-flat) r*_l >= r_l/2 for every l in P (r*_l computed with B'): the targets of later B'-carriers carry at most half of the room of S_l;
 (b) c(delta) + Delta <= theta(l_*) T_lo(l_*)^2 with theta(l_*) := C(T_lo(l_*)^{1/2} + 4^{-n^w_{l_*}} T_hi(l_*)^2) -> 0, and Delta <= c_f;
 (c) consequently, if along infinitely many unblocked windows l_j the remaining hypotheses of Proposition T hold — (S-flat), (H1),
     (H2), (H3) for B'_j, the status part of (BS) with a uniform gamma_B, and (HF) with C^#_{H,j} <= F(l_j)^{1/2} — and the B'_j-dependent
     constants of fixes T4, T6 satisfy C_0^# + sum_{l in B'_j, nondeg. peak} 1/mu_{k(l)} <= F(l_j)^{1/4}, then f in Rec.
Proof. (a) For l in P, r*_l >= r_l/2 >= u delta°_l/2, and 1 + 6/(u delta°) <= (7/u)(1 + 2/delta°) (u <= 1). For l in B', r*_l :=
||v_l 1_{S_l\F}||_1 (fix T2; for l in B the note's 2||v|| is even better) >= c_F delta°_l, where c_F > 0 accounts for the finitely many S_l
meeting F; so 1 + 3/r*_l <= (3/c_F)(1 + 2/delta°_l). Multiplying, Lambda* <= (7/u)^{|P|}(3/c_F)^{l_*} Lambda°(l_*) and u^{-|P|} <= u^{-l_*}
= F^{1/4}. Hence K_* T_hi(l_*) <= C_f^{l_*} F(l_*)^{-3/4} -> 0 and n^w_{l_*}/K_* >= F(l_*)^{3/4} C_f^{-l_*} -> infinity.
(b) delta lives on the sets S_l \ F, l in E, with |delta_s| = 1 - eps_l z_s and r_l = sum_s v_l(s)|delta_s|, so |delta_s| <= r_l n_l 2^s/delta_l.
For a carrier l'': the signature part of u_{l''}(delta) vanishes unless l'' in E, where it is eps r_{l''}/... of modulus <= r_{l''}; the target
part sees S_l only if l < l'' (allowedness (a)); for l'' <= l_*, |y_{l''}(delta)| <= ||y_{l''}||_1 max{|delta_s| : s <= s_max(l_*), s in S_l, l in E}
<= (5/4) max_E r_l 2^{s_max(l_*)}/delta_min(l_*). Since r_l <= rho_l delta°_l <= b(l_*) for l in E (delta° <= 1):
sum_{l'' <= l_*} min(lambda_{l''}, |u_{l''}(delta)|) <= 3 l_* b(l_*)(1 + 2^{s_max}/delta_min) <= 6 * 4^{-2n^w} T_hi^4 = 6 * 4^{-n^w} T_hi^2 * T_lo^2,
while carriers l'' > l_* contribute <= sum_{l''>l_*} lambda_{l''} <= T_lo(l_*)^3 ((P2)). The same bounds give Delta <= (tiny) + 2 T_lo^3, so
Delta log(e/Delta) <= C T_lo^3 log(1/T_lo) <= C T_lo^{5/2}. Summing gives (b); Delta <= c_f for l_* large.
(c) Proposition T applies at f^#_j with these K_*, theta (pinning (P) holds with K_* by (S-flat); (BS)-cost by (b)); with fix T6 its
frozen-error constant is K^#_* <= K_* + F^{1/4} <= 2 C_f^{l} F^{1/4} Lambda°. Corollary 3.4 needs (1 + C_H)K^#_* T_hi -> 0 and
n^w/((1 + C_H)K^#_*) -> infinity, which hold since (1 + F^{1/2}) 2 C_f^l F^{1/4} Lambda° / (F Lambda°) <= 4 C_f^l F^{-1/4} -> 0;
(E-e) holds with theta_j -> 0. QED

## 4.4 Assessment.
* For (D1^F) the band of Z3 4.3(ii) never occurs at unblocked windows, and unblocked windows exist for every f (Proposition 4.2.1).
  So Z3's "main obstacle" 7.1 is an artifact of the window-length function l 2^{l^3}.
* What remains of (O1)(i) for (D1^F) is EXACTLY the companion-cone problem for the growing finite sets E_j of nearly exactly swallowed
  carriers: slaving conditions ((S-flat), (H1)), non-degeneracy ((H2), (H3)), status stability ((BS)), and a Hoffman bound
  C^#_{H,j} <= F(l_j)^{1/2}. This is the same type of difficulty as the open part of Theorem thm:S (Remark rem:S(c); (O2) with exact
  swallowing): (O1)(i) merges into (O2) for the explosive design.
* It does NOT solve (O1)(i): Hoffman constants are f-dependent and cannot be dominated by a design function chosen before f; and by
  Z3 Lemma 1.4 an E-carrier that is d-neutral at f with positive defect makes the cone at f^# degenerate (C_H >= |R^**zhat^#|/Re(u_l),
  with Re(u_l) <= b(l_*) — astronomically large). Re-tuning e (Z3 4.3(iii)) has only |F| - 1 degrees of freedom while supp a = F is
  kept (needed for Lemma U), so at most |F| - 1 such carriers per window can be re-tuned without adding base coordinates.
* Status: PROVED: Lemmas 4.1.1, 4.1.2, Propositions 4.2.1 and 4.3.1 (as a conditional statement). HEURISTIC: that (HF) with
  C_H <= F^{1/2} is "typical" (it holds e.g. when, in every block, the E-carriers are strict non-peaks whose weights q_l are bounded
  below by a design function of l and all have the same sign — then the projection is the explicit d-pinning tau_l <= O(K_* t)/q_l —
  but status stability and slaving remain to be checked case by case).
