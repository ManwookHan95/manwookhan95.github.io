# Z3 part 7 — main obstacle, corrections to the note, next steps

## 7.1 Main obstacle (precise). OPEN.
All proved recovery mechanisms for the SLD operator are WINDOW methods: on a window of n dyadic scales [T_lo, T_hi], every coarse
carrier must be either pinned (frozen error ~ t/r_l, requiring n >~ K = product (or at best max) of 1/r_l) or exactly switched at
the working first row (exact at f, or at a companion f^# whose cost must be o(T_lo^2) = o(4^{-n} T_hi^2) by Theorem E). For a carrier
of room r_l, exactification costs ~ min(lambda_l, r_l) (Lemma 3.1, unweighted; numerically sharp). Hence a carrier whose room lies in
the band T_lo^2 << r_l << 1/n defeats every window method, and for f with infinitely many carriers whose relative rooms decay
super-geometrically but without tower gaps (e.g. r_l = 2^{-l^4} delta°_l) every window contains such carriers. By Proposition 4.2 this
is exactly a lower-semicontinuity question along the far lowerings f^L (or the peak-ifications of 6.1): is dist(rho g, C(f^L)) -> 0?
The single scale responsible is the transition scale t*_l = sqrt(lambda_l r_l) of each band carrier, where its switching
(<= min(t/(q_0 r_l), 6 lambda_l/t)) peaks at ~ sqrt(lambda_l/r_l) = t*_l/r_l.

## 7.2 Corrections / precisions to the note's Remark rem:openZ (O1). PROVED.
 (a) (O1)(i) concerns only INFINITELY many approximately swallowed carriers (Proposition 4.1); with finitely many, Theorems thm:Bpm,
     thm:S apply as they stand, whatever the rate |z_j| -> 1 or the position of the sign changes.
 (b) (O1)(ii): weak bad peaks and near-threshold bad strict non-peaks are obstacles only for infinitely many bad carriers (5.0); bad
     peaks are pinned (additively) by their inverse margins (Theorem 5.4); (H2) and (H3) can be weakened per block (Theorem 5.3).
 (c) "Approximately two-piece data" cannot be fed to Corollary cor:D1 at f: the kink of Remark 1.5 is unavoidable for defects
     proportional to the scale; the right formulation moves the first row (Theorem E) and is then limited by the band (4.3).
 (d) Lemma 1.4: exactifying a d-neutral, approximately resonant carrier at a companion with the same base part destroys its
     d-neutrality by exactly its room; Remark rem:thmM's "finitely many inexact coordinates (equations instead of inequalities)" works
     only while the inexact coordinates are finitely many AND the d-rows stay well conditioned.

## 7.3 Next steps (suggested).
 1. Lower semicontinuity along far lowerings f^L at (W+-)-failing points: compare the two-sided decompositions of g at f and at f^L
    scale by scale; the fine carriers l > L are pinned at f^L with GOOD constants, so the question is whether g's switching through
    l > L (at scales <= C lambda_l <= C c_{L+1}, far below the slack threshold sqrt(c_{L+1})) can be replaced at f^L by two-sided block
    usage at second-order cost — this needs the switching amplitude through l to be o(1) at those scales, a statement about g, not f.
 2. A multi-level averaging in which a band carrier's frozen error enters through log(1/r_l): average separately the scales below and
    above t*_l and glue with the slack of a SECOND parameter (two nested windows); the obstruction in 4.3(ii) is a single scale per carrier.
 3. Re-tuning the Hilbert part (4.3(iii)) to make the companion cones of d-neutral approximately resonant carriers non-degenerate.
 4. The tuning lemma for degenerate peaks (5.5(ii), 6.1): a first-order genericity statement for the clamp equation of a block.
 5. Shifted (infinitely supported) two-piece data for (H2)-failing blocks with non-d-neutral switching (5.6(b)), in the spirit of the
    shifted certificates of Section sec:certificates.
