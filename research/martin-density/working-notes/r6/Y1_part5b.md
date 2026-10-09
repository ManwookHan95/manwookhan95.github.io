# Y1 part 5b — The master theorem for D_X, corollaries, and the exact residual list

## 5.3 Theorem E' (window-dependent constants).  PROVED.
Z3 Theorem E holds with (E-b) read with the coordinate kinds [1]-[3] of Proposition 5.2(iii), with A_2 fixed and gamma_B = gamma(w_j)
allowed to depend on j, and with (E-d), (E-e) replaced by
 (E-d') K_j T_j -> 0 and n_j >= 48 rho^2 K_j/(c_{flat,j}(1 - rho^2)) for large j, c_{flat,j} := c_flat(A_2, gamma(w_j)) >= c_0 gamma(w_j)/A_2;
 (E-e') eps_j := p*(f_j - f) <= min{c_{flat,j}^2 (1-rho^2)(T_j 2^{-n_j})^2/(24 rho^2), (1-rho^2) r_0^2/6}  (r_0^2 = 1 - rho^2).
Proof.  Lemma U (Z3) extends to kind [3] (inward-only) coordinates: Z6 referee Lemma 2.1 (block step: ||W||_inf = (1 - rd)M because
inward coordinates move toward 0 and c_flat A' <= M/4; first-order term s omega(k) alpha(k) = 0 at strict non-peaks).  In Lemma U the
constants A_2, gamma_B enter only through upper bounds on c_flat (c_flat <= gamma_B/(2A_2), c_flat <= C_min/(2A_3), c_flat A_2 <= M_min/4,
relative errors O(A_3 c_flat)); t_1 and j_0 are constrained only by r^4-terms and the convergence of the scalar and transfer data of
f_j -> f (Z4 Step 7, verified by the Z4 referee, Section 8).  In the proof of Theorem E (Z3 2.2), after j is fixed, c_flat enters only
through (A), through I_r := {i : c_flat t_i < rho|r|} with sum_{I_r} t_i < 2 rho|r|/c_flat, through 2rho^2 K r^2/(c_flat n) <= (1-rho^2)r^2/24,
and through eps_j < theta_j rho^2 r^2/c_flat^2 when I_r != {} — exactly (E-d'), (E-e').  Corollary cor:D1 is applied at f_j to the averaged
data, which are two-piece data at f_j (kind-[3] coordinates are strict non-peaks of f_j).  QED  (Same statement: Y2 Theorem E'.)

## 5.4 MASTER THEOREM (design D_X).  PROVED (from Theorems 1, 2, E', Lemmas 3.1-3.6, 4.1-4.3, 5.1, Proposition 5.2).
Let T = D_X, N >= 1, and f in S_{p_N^*} with finite base support F.  Suppose that for infinitely many levels l there is a clean
sub-window w(l) of level l (one exists at EVERY level, Theorem 2) at which (SP_w), (Do_w), (Cmp_w) and (NN_w) hold.
Then f in Rec: (f, g) in cl NA((c_0, p_N), l_2^2) for every g in C(f).
NO RATE CONDITION is imposed: rooms of signature sets (good or slaved), rooms at target coordinates, margins (weak, degenerate),
gaps (near-threshold carriers of both types), d-coefficients and their relative sizes, the number of swallowed carriers, slaving,
(H1), (MS) and contact sets are arbitrary; at each used window every rate is either robust (absorbed by the design) or tiny
(closed, shifted, pinned, or compensated).
Proof.  Fix g in C(f), rho in (0,1), eta_0 in (0,2] with rho^2(1 + eta_0) <= (1 + rho^2)/2, kappa_0 := (sqrt(1 + eta_0/2) - 1)/2, eta <= eta_*
with eta_Gamma(eta) <= 1 and sqrt(1 + eta_Gamma(eta)) <= 1 + kappa_0/2.  Along the given levels l_j -> infinity take w_j := w(l_j),
f_j := f^#_{w_j} (part 4), T_j := T_hi(w_j), n_j := n(w_j), and for each dyadic t in W(w_j) the functional g_{j,t} := g_t of
Proposition 5.2 (built from a two-sided decomposition of g at f at scale t).  Check Theorem E':
 * supp a_j = F; f_j -> f since p*(f_j - f) <= theta_{w_j} T_lo(w_j)^2 -> 0 (Lemma 4.1).
 * (E-a): b^+-(xi_j) = 0, t||b^+-||_1 <= A_0, and Gamma^{(j)}_w <= (1 + kappa_0/2 + C theta_{w_j} + K_{w_j} t)^2 <= 1 + eta_0/2 once
   C theta_w + K_w T_hi(w) <= kappa_0/2 (true for large j, below).  (E-b): Proposition 5.2(iii), A_2 fixed, gamma(w_j) = min M u(w_j)/4.
 * (E-c): p*(g - g_{j,t}) <= K_{w_j} t.
 * (E-d'): K_w <= C_f Design(l)^3 u(w)^{-3} (Y1_part5c 5c.2) and c_flat(w) >= c_f u(w), so with Q(w) = Design(l)^4 u(w)^{-omega(l)-8}:
   K_w/c_flat(w) <= C_f Design^3 u^{-4} = C_f Q(w) u^{omega+4}/Design <= C_f Q(w) u(w), while n(w) >= l 2^{l^3} Q(w); hence
   n(w) c_flat(w)/K_w >= l 2^{l^3}/(C_f u(w)) -> infinity.  K_w T_hi(w) <= C_f Design^3 u^{-3} 2^{-l^3}/(l Q(w)) <= C_f 2^{-l^3}/l -> 0.
 * (E-e'): eps_j <= theta_w T_lo(w)^2 with theta_w = C_f T_lo(w) log(1/T_lo(w)), and c_flat(w)^2 >= c_f u(w)^2, while T_lo(w) <= 2^{-n(w)} <=
   2^{-u(w)^{-4}}; so theta_w <= c_f u(w)^2 (1-rho^2)/(24 rho^2) for large j.  Also eps_j <= (1-rho^2)r_0^2/6 eventually.
Theorem E' gives (f, rho g) in cl NA; rho < 1 was arbitrary.  QED

## 5.5 Corollaries
**Corollary M1 (maximal contact).  PROVED.**  Let F be finite and z = eps_0 on N \ F.  Then f in Rec provided, for infinitely many
levels, at a clean sub-window w: every block is compensated at w (e.g. (DR) of Z4) or sigma-one-signed at w, and in every
sigma-one-signed block no coarse carrier l'' with 0 < sigma q_{l''} and rho_{l''} <= b(w) exists, and if one with sigma q_{l''} < 0,
rho <= b(w) exists then (Rep^sigma_m) holds at w.  In particular weak and DEGENERATE swallowing-type peaks, near-threshold carriers of both types, and all rooms are harmless at
maximal contact (cf. Z4 Remark 5.5 and Z6 referee Proposition R1, where degenerate positive peaks at maximal contact were open).
Proof.  Every carrier is exactly swallowed (class G, r^nat = 0) and T(l) \ F consists of contacts, so (C1), (C2) are void; hence
u_{l''}(zhat^#) = u_{l''}(zhat) for every non-donor coarse l'' and q^# = q A/A^#: exactly d-neutral carriers stay exactly d-neutral, and
(NN_w) is the stated condition.  (SP_w): by Z4 Lemma 5.0, every block has non-degenerate peaks with w = eps_0 M (swallowing type,
margin >= q_0/4: a LOWER source (L2) once u(w) is below the fixed relative margin) and with w = -eps_0 M (anti type: UPPER (U2)).
(Do_w): the anti-type peaks are donors (part 4.1).  QED
**Corollary M2.**  Let F be finite.  Suppose every block m has fixed repair directions of both signs ((DR^+_m) and (DR^-_m), nonzero),
every block has an exactly swallowed anti-type peak (UPPER source and donor) and an exactly swallowed swallowing-type peak with
positive margin (LOWER source).  Then f in Rec.  PROVED (Theorem 5.4: by Lemma 5.1' every block is compensated at every clean w of
large level, so (Cmp_w) holds and (NN_w) is void; (SP_w) and (Do_w) hold by the fixed peaks).  Compared with Z4 Theorem A'' (read
for D_X), the hypotheses (H3) (no degenerate swallowing-sign peaks) and the growth condition (W_inf) (margins, gaps, target rooms,
good rooms) are dropped; a donor replaces (H3).
**Corollary M3 (what the master theorem adds to Round 5).**  For D_X the rate items of the consensus core (r) of ADDENDUM 5 (rooms of
good sets incl. approximate swallowing (O1)(i), margins of non-rigid swallowing-type peaks K_P, gaps gamma_B of kept q < 0 carriers,
rooms gamma_T at target coordinates, relative Farkas/d-coefficients K_nn in the COMPENSATED and in the "opposite-sign" direction of
one-signed blocks) are no longer obstructions; item (d) (degenerate non-rigid swallowing-type peaks) is removed whenever the block has
a donor (always at maximal contact).  PROVED (by Theorem 5.4: each was a failure of a growth condition that 5.4 does not need).

## 5.6 The exact residual list (F finite; design D_X).  OPEN.
Lemma Z (density for p_N) for D_X can fail only at pairs (f, g), g not window-pinned, with f such that at all but finitely many
levels, EVERY clean sub-window w violates one of:
 (n)  [directional nearly neutral resources] a sigma-one-signed block has a KEPT carrier (rho^#-tiny strict non-peak) with d-coefficient
      of sign sigma at f^#_w (or of sign -sigma without (Rep^sigma_m) at w).  Sources: carriers nearly neutral at f with the block's own sign
      (the K_nn rate in its uncompensable direction), Z3 Lemma 1.4 carriers (d-neutral, approximately resonant: q^# = r^nat/A^# > 0,
      Lemma 4.3), d-neutral kept carriers whose targets meet (C2)-raised near-contacts.  Removing it needs either LOWERING a z-signed
      functional (impossible with banks for diagonal U, Y4 Prop. 2.8; with supp a fixed only |F| - 1 Hilbert directions), or a pinning
      statement of Conjecture G type for nearly neutral carriers.
 (m)  [mixed blocks] a block is neither compensated at w ((Rep^+) and (Rep^-)) nor one-signed at w (Y2 Theorem M, unrefereed, reduces this
      to ray rates and a d-forced-face Farkas constant; multi-block rays remain, Y4 (m')).
 (d)  [aligned corner] a block that is not one-signed and contains near-threshold swallowing-type carriers has no donor: every
      non-degenerate peak c of the block with S_c ∩ F = {} has infinitely many s in S_c with vs_c z_s > 0 (coordinates of its OWN
      sign: contacts or free).  Then no signature move of a peak raises the threshold with a design-controlled range.  (The Y2 referee's
      "target donors" (free target coordinates with positive one-sided threshold derivative) would shrink this further; not used here.)
 (h)  [shift pinning] (SP_w) fails: some block lacks an UPPER or a LOWER source (Y2 Theorem H, unrefereed: shift costs).
 (O4) F infinite (Z5 and Y3, separate).
Remarks.  (3) (SKETCH) In (n) the imbalance to be repaired is TINY: |Q^#_m(tau_0)| <= sum_{kept} |q^#| tau'_0 <= C l b(w) D(l)/t, so a repair
direction with |d-sum| ~ Phi M/(mC) needs amounts c <= C l b D^2/t, i.e. |omega| <= C l b D^3/t, and the one-sided expansion at a q < 0
member then needs only gap^# >= C l b D^3 (not a robust gap).  Hence a RESONANT near-threshold anti-type peak, converted by a threshold
raise into a strict non-peak with gap^# ~ M delta ~ T_lo(w)^3 >> l b D^3, can serve as a negative repair direction for (n).  This shrinks
(n) to blocks without such carriers; the bookkeeping (a second kind of (Rep) with amount-dependent gap) is routine but not written.
(1) Nothing in (n), (m), (d), (h) is a rate: each is a structural/directional property of the configuration at a level,
which no design can absorb by lengthening windows.  (2) A counterexample to density for D_X would have to live in one of these
classes; nothing found here points to one (all single-module mates are certificates, Z6 6.2; the directional obstruction (n) concerns
the METHOD: exact data at a companion with the same base part).
