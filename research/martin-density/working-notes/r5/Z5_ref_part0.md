# Z5 referee: reading log (part 0)

Key facts from the note (martin_density_note.tex), for later checking:
- thm:windowed (l.4489): needs F finite; last step uses thm:transfer (transfer peaks) which needs a in c_00.
- lem:uniformtransfer (l.4438): F finite; (C-a) ||b||_1 <= A_0, Gamma_w <= 2; (C-b) block conditions. Base: no flips needs
  c_flat t_1 A_0 <= min(a_min, ...); supp b in F.
- prop:windowcert (l.4344): b_t := B_+ 1_F - a_t a, uses lem:finitebase (F finite) for ||b_t||_1 <= K_b.
- lem:flip (l.4863): F may be infinite. f^±_j, g_j, clamp b^cl(j) = sgn(B_+(j)) min(|B_+(j)|, 2|a_j|/t);
  ||(B_+ - b^cl)1_F||_1 <= ||Delta B 1_F||_1 + t/(2 q_0).
- lem:boundedfree (l.4904): F finite; injectivity uses a in c_00 (Y cap c_00 = {0}).
- lem:rigidity(a) (l.294): needs b_+ - b_- in c_00.
- thm:Bstar (l.4956): F finite; window-pinned def l.4944.
- lem:signmixed / thm:Bpm: F finite; rooms on S_l \ F.
- thm:S (l.5579): F finite; R_S defined in def:swallowed (l.5148).
- rem:Binf (l.5661): sketch; step (iv) = thm:transfer for a not in c_00 and b finitely supported: NOT proved in note.
- rem:openZ (O4): F infinite without room.
- lem:budget(b),(d), lem:switchbudget: valid for any F? (check: lem:budget assumes nothing on F? it's in "any admissible T" subsection, f arbitrary; eta_* uses nu).
- lem:smallness: any f.
- lem:suplevel: any f.
- prop:pinned: f in R_0 (F finite by def of R_0), but proof of (a) uses only lem:budget(b) & disjointness.

## Preliminary checks (after reading Z5_notes.md once)
- T1: checked Steps 1,4,5,6 with a -> a_N: bookkeeping identity is at x'_N, a_N(x'_N) = c_N, e_{m,N} -> e_inf uses
  R_m* y_{m,N} -> R_m* y_m in l1 and a_N -> a. No-flip radius uniform in N (|b'_N(j)| <= (C c^a_N + |kappa_N|)|a_N(j)|).
  E may be negative: (1+E) >= 1/2 fine. VERDICT so far: correct.
- T3: rebalancing error |lambda| 2 q*(rb) <= 6|I|K3 KY (1+||U||) c_flat r^2. ok.
- T4: identity for (b^cl 1_{F_t})(zhat) ok; kappa bound ok; b_t ratio <= 3/t ok.
- T7b: r^{[M]} DEcreases in M; M(T_lo(l*)) is the largest needed and the smallest room -> (W^c) correctly uses it.
- T9: verified (a) via base identity; (b) Fl^M(t) = sum 2(-s_j t rho b_j - lambda_M |a_j|)_+ <= rho Fl_b(t). ok.
- T10: Phi(c) injective via first-order coordinate (sum c u)(zhat). ok. Phrase "rigidity(a) fails" is loose:
  the lemma as stated (b_+ - b_- in c_00) holds; what fails is uniqueness for base parts in l1(F cup K).
- T11: ok (constants check).
- T13a: ok, tautological composition.
- T14: D*/t -> infinity holds for EVERY support-swallowed carrier (also cushion-dominated, D* >= 2c/t);
  general proof: Phi(Kt,t) <= Kt m_l(Kt^2/2) = o(t). The distinguishing feature of fast swallowing is not D*/t but
  the impossibility of exact (flip-free) data (T15). "windowed averaging cannot apply" is overclaimed (only the
  pinning route fails). Exponent requires S dense-ish (v ~ 2^{-j} on all large j of S).
- T15: Lemma 7.4 ok; necessity of (sX)_- <= 2A holds for ANY data with b+ - b- = X on F (not just common shifts).
- T16: trivial, ok.
