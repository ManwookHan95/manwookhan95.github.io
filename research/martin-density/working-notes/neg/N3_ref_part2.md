# N3 referee — part 2: Lemma 2.0, Lemma 2.2, Theorem 2.3, Corollary 2.4, Corollary 2.5, Theorem 2.6

## R2.1 Lemma 2.0 — CORRECT (re-derived: 1-Lipschitz minimum; minimizer bound |c'| <= 2||h1_S||/||psi'1_S||;
breakpoint evaluation for |S| = 2).

## R2.2 Lemma 2.2 (collective motion of weighted peaks) — CORRECT (re-derived)

q_0 G_b + sigma' G(W+-) <= e (proof of Lemma 1.2), [I, lem:bookkeeping(c)] keeps a single peak term
|alpha'(k)|(||W||_inf - s_k W(k)) >= 0, ||W+||_inf >= M' + t L+ and ||W-||_inf >= M' - t L-.  All signs check.
 P2.1 (weighted form; important).  By [I, eq:margin], sigma'|alpha'(k)| = lambda_k mu'_k (mu'_k = margin of k at f').
      Hence the bound reads  lambda_k eps+-_k <= e/(t mu'_k) <= t/(2 mu'_k)  for mates, and always
      lambda_k eps+-_k <= 2(2 + e) lambda_k / t.  A peak of tiny WEIGHT but robust MARGIN is therefore as well
      controlled, after weighting, as a robust peak.  N3 classifies peaks by alpha' (weight x margin) instead of by
      margin, and this is the source of the defects found in R2.3-R2.5.

## R2.3 Theorem 2.3 (positive-scale profile bound) — CORRECT AS STATED (re-derived line by line); lossy; see R2.4

Re-derivation: beta+-_j = -d+- psi'_j + r+-_j with |r+-_j| <= (|L+-|/M' + ||Omega+-||_inf) eta_j + t nu_j/(2 sigma' alpha_0)
<= 7.5 eta_j/t + t nu_j/(2 sigma' alpha_0) (|L|, ||Omega|| <= 2.5/t, M' > 0.71 since C <= ||Phi||_2 <= 12^{-1/2});
sandwich -d+ - X+_j <= pi(j) <= -d- + X-_j on aligned S; anchor |pi(j_f) + d+-| <= (|B+-_{j_f}| + eps+-_{j_f})/|psi'_{j_f}|;
budget: r_f(|B+_{j_f}| + |B-_{j_f}|) <= t/c', S-terms <= t/c' + 2 mu_S/t (the two budget uses overlap; this only loses a
factor 2).  The constants A, H and the final sqrt-form are correct.

## R2.4 MAJOR: exact visibility is impossible for every admissible T (Corollary 2.4 is vacuous)

LEMMA R-V (no exact visibility).  PROVED.  Let T be admissible, I = {1}.  (a) For every coordinate j the set
{k : u_k(j) != 0} is infinite.  (b) At every row f' and for every alpha_0 > 0, at most 1/alpha_0 peaks have
|alpha'(k)| >= alpha_0.  (c) Hence for every Z != {} and all visibility data (Lambda, alpha_0) of Definition 2.1,
H > 0; "Z exactly visible" never holds.
Proof.  (a) By (T-d) every tail {u_k : k >= n_0} is norm dense in S_{q*} ([I, def:admissible] and the remark after
it).  G_j := {v in S_{q*} : v_j != 0} is relatively open and nonempty (it contains e_j*/q*(e_j*)), so every tail meets
it.  (b) ||alpha'||_1 = 1 [I, lem:threshold].  (c) Lambda is finite by (b); by (a) some k notin Lambda has u_k(j) != 0,
and lambda_k > 0, so eta_j > 0.  QED
Consequences.
 (i)   Corollary 2.4 has a hypothesis that no admissible T satisfies; its "strengthening of [II, cor:II-S1]" is void.
       Verdict: WRONG as a strengthening (a vacuous truth).  Cor S1 assumes exact two-piece data, under which ALL peaks
       (cofinitely many, almost all with alpha -> 0) act through the single term -d psi — an algebraic locking that no
       carrier-by-carrier positive-scale argument with alpha-classified peaks reproduces.
 (ii)  Every "exact visibility" clause in N3 is vacuous: Theorem 2.6(a) second sentence, Corollary 2.8, Theorem 3.1(iii)
       (there it is also unused in the proof), the closing remark of the proof of 2.6(b2) and the Fact used there.
 (iii) The "sqrt(mu) law" Osc <= 2(2 A mu_S)^{1/2} of §0, §3.3 holds only in finite models; for admissible T the bound is
       2(A(2 mu_S + 15 H))^{1/2} with an intrinsic floor 2(15 A H)^{1/2} > 0 at mu_S = 0.
Numerical sanity check (N3_ref_work/floor_check.py; N3's finite model plus ONE extra low-weight carrier k6 seeing S):
   k6 a STRICT NON-PEAK (u6 ~ e1 - e2, u6(xhat) = 0):  Osc_max(m=0) = 4.6e-2, 2.3e-2, 1.0e-2 for lambda6 = 2e-3, 5e-4, 1e-4,
       i.e. Osc_max / sqrt(H6) = 1.14 (constant): the floor is GENUINE and sharp in its scaling for strict non-peaks;
   k6 a low-weight PEAK with robust margin (u6 ~ e1 - 0.5 e2): Osc_max(m=0) = 1.9e-4, 0.9e-4, 1.8e-4 (grid level, baseline
       4.9e-5): Osc/sqrt(H6) <= 0.02 — the floor is an ARTIFACT for robust-margin peaks (they are locked, P2.1);
   with banks m = 1e-4 both cases give Osc ~ 1.6-1.9e-2, as in N3's baseline (1.4e-2).

## R2.5 Repair: Theorem 2.3' (margin-classified visibility) — PROVED here (full proof in N3_ref_notes §2)

Classify peaks by margin.  For mu_0 in (0,1] let N_{mu_0}(f') := Q' u {k in P' : mu'_k < mu_0} (strict non-peaks and
small-margin peaks) and eta_j(mu_0) := sum_{k in N_{mu_0}} lambda_k |u_k(j)|.  Then for every t in (0,1], under the
hypotheses of Theorem 2.3 (no Lambda, no alpha_0),
   sum_S |g'_j - pi(j_f) psi'_j| <= t [ rho_S/(c' r_f) + 1/c' + 2 (rho_S + |S|) l(t)/mu_0 ] + (2 mu_S + 15 H(mu_0))/t,
   l(t) := log_2(1/t) + 2.2,     H(mu_0) := rho_S eta_{j_f}(mu_0) + sum_S eta_j(mu_0).
Key step: for robust-margin peaks lambda_k eps_k <= min(t/(2 mu_0), 5 lambda_k/t), and sum_k min(t/(2mu_0), 5 lambda_k/t)
<= t l(t)/mu_0 because lambda_k <= 2^{-1-k}.  Low-weight robust-margin peaks no longer enter the floor.
Still H(mu_0) > 0 for admissible T (tails approximate every v with v(xhat') = 0, v_j != 0, and such u_k have small
margin or are strict non-peaks): Lemma R-V persists in the margin form, but the floor is now the weighted density of
NEAR-KERNEL carriers (u_k(xhat') ~ 0), which (MS)-type sparsity can make o(mu_0).

## R2.6 Corollary 2.5 (inheritance) — CORRECT for the Theorem 2.3 functional; extension and limits

The continuity facts used (z' -> z coordinatewise, psi' -> psi in l_1, c', sigma', margins of fixed peaks, a' -> a in l_1)
are [I, prop:continuity] and eq:margin; a robust peak of f stays a peak with alpha' >= alpha_0 nearby.  Correct.
LEMMA R-F (Fatou inheritance of every missed-weight floor).  PROVED.  For fixed mu_0 > 0, j, and f'_n -> f:
   liminf_n eta_j(mu_0; f'_n) >= eta_j(mu_0; f).
Proof: membership in N_{mu_0} is an open condition in the forced data (k in Q: |zeta(k)|/sigma < Phi_k^2 M/C, strict;
k in P with mu_k < mu_0: |xi(u_k)| - vartheta Phi_k < mu_0, strict), both sides converge for fixed k, so every k in
N_{mu_0}(f) lies in N_{mu_0}(f'_n) for large n; apply Fatou to sum_k lambda_k|u_k(j)| 1[k in N_{mu_0}(f'_n)].  QED
Hence Theorem 2.3' (fixed mu_0) is inherited exactly as Theorem 2.3 is: N3's inheritance conclusion extends to every
positive-scale sandwich with a FIXED classification threshold.  What is NOT inherited is the limit mu_0 -> 0 at a fixed
C-tame row, i.e. the EXACT mechanism (Prop. 1.7(c), Cor S1, Prop S3), which is the mechanism of Theorem NL.
 P2.2  N3's sentence "a FIXED free coordinate of f can never produce a uniform obstruction" is proved only for Theorem
       2.3-type bounds.  For the exact mechanism it is UNPROVED and its natural version is false as a mechanism
       statement: if g has different profiles at two free coordinates j, j' of f outside the supports of the strict
       non-peaks of f (allowed at a non-tame f by its floor), then at EVERY C-tame NA row f' near f with j, j' notin
       Sigma'(f') one has dist_{p*}(rho g, C(f')) >= (2/3) rho |psi(j) psi(j')| |pi_g(j) - pi_g(j')| - o(1)
       (Prop. 1.7(c): g' = -d' psi' off Sigma'(f'), plus the Lambda-functional argument of [II, prop:II-S3] with
       s_1 = j, s_2 = j').  Free coordinates of f
       CANNOT be banked or made contacts by nearby rows (z'_j -> z_j, |z_j| < 1; N1-ref P-1b).  So the escape is only
       by COVERING (j in supp u_k for a strict non-peak k of f') or by non-C-tame approximants.

## R2.7 Theorem 2.6

(a) CORRECT in its first (general) form A_n(j)(2 mu_S + 15 H(j)) >= kappa^2/5.  The "exact visibility" form is vacuous.
    Correct replacement (PROVED, two lines): call a free coordinate j of f'_n kappa-CLEAN if 150 A_n(j) H(j) <= kappa^2;
    then mu_S(f'_n) >= kappa^2/(20 A_n(j)) for every kappa-clean j; and by Theorem 2.3 at f, if S subset K, no
    j in J(f) is (kappa)-clean at f (else Osc_S(g; psi) <= 0.64 Osc_S(g; psi)).  "A_n(j) <= C(1 + rho_S/r')" holds with a
    j-dependent C (the nu-term needs nu_j/|psi'_j| bounded).
(b1) CORRECT (AM-GM, A >= ||psi'1_S||/(c' nu^tot_j), |psi'_j| <= nu^tot_j).
(b2) CORRECT AS LITERALLY STATED (Theorem 2.3 bounds only, the FIXED set S, Lambda subset {lambda_k >= eps} with eps fixed
     before (theta, N)); N1 Lemma 1.4 is refereed (N1-ref: correct with fixable gaps, banks allowed only on F, on
     contacts with the contact sign or beyond the window — S subset K u F complies).  Gaps:
     G2.1 The interpretation "NL is not uniform / the profile mechanism is defeated" does NOT follow.  At a C-tame
          banked truncation f'_{theta,N} the exact mechanism forces g' = -d' psi' on all of N \ Sigma'(f'), and banks only
          on S leave every other oscillation pair of g outside Sigma': for any mate whose profile pi_g = g/psi is
          non-constant on K \ S (e.g. a switching mate whose split varies along an infinite contact set), pick
          {s_3, s_4} subset K \ S with pi_g(s_3) != pi_g(s_4); Prop. 1.7(c) and the functional
          Lambda'(h) = h(s_3) psi'(s_4) - h(s_4) psi'(s_3) of [II, prop:II-S3] (|Lambda'(h)| <= ||h||_1/2,
          dist_{p*} >= dist_{l1}/3) give dist_{p*}(rho g, C(f')) >= (2/3) rho |psi(s_3) psi(s_4)| |pi_g(s_3) - pi_g(s_4)| - o(1)
          along these rows (whenever C-tame and s_3, s_4 notin Sigma').  So per-S banking is insufficient; one must bank the whole
          oscillation set inside [1, N] with summable masses (what [I, def:engineered] does: masses on ALL window contacts
          with b^theta != 0).  With that change the contact part is fine; the free-coordinate part (P2.2) is not covered.
     G2.2 The "costs nothing essential" remark on Lambda subset {lambda >= eps} is heuristic (uniformity in eps is the same
          issue as (b3)); with Theorem 2.3' (margin form) the restriction becomes unnecessary for robust-margin peaks.
(b3) SKETCH — label appropriate.

## Summary of part 2
Correct: Lemma 2.0, Lemma 2.2, Theorem 2.3, Corollary 2.5, Theorem 2.6(a) first form, (b1), (b2) literally.
Wrong/vacuous: Corollary 2.4 (exact visibility impossible, Lemma R-V); every exact-visibility clause; the sqrt(mu) law
for admissible T.  Overstated: identification of Theorem 2.3 with the NL mechanism; "a fixed free coordinate of f can
never produce a uniform obstruction"; the reading of 2.6(b) as "NL is not uniform".  New: Theorem 2.3' (margin form),
Lemma R-F (Fatou inheritance), the free-coordinate covering alternative (P2.2).
