
# U2 part 5: numerics (evidence only) and what remains

## 5. Numerics: r8/U2_work/pair_tuning_check.py (mpmath, 60 digits)
Finite model of the value map val_k = u_k(zhat), zhat = z + U e, e = U^* a/||U^* a||, z = sgn a on F, diagonal base mu_s = 2^{-(s+1)^{1.5}},
14 support coordinates, one owner carrier with signature on {5, 7, 9}, six other carriers vanishing there.  Pair move at s = 5 < s' = 9
with Delta = -(alpha_{s'}/alpha_s) Delta' (Lemma TR-inf (c)):
  Delta' = +-1e-6: owner change matches the predicted (mu_{s'}^2 v(s')/nu)(1 - rho_{s'}/rho_s) Delta' to relative error 1.5e-14;
                   maximal change of the other carriers 3.4e-31 (second order);
  Delta' = +-1e-9: relative error 1.5e-17; others 3.4e-37 (scales as Delta'^2).
A single unpaired move at s' changes the other carriers by 2.4e-25 >> the owner's own change 3.6e-27: the common term dominates for a
thick coordinate, which is why single support moves are not admissible tuning resources (part 3.2, 4.3(a)).

## 6. What remains open after U2 (designed norm T_final^*, finite I)
Density of NA((c_0,p_N), l_2^2), Lemma Z, and density for Martin's p remain OPEN for every admissible T.  For INFINITE base support:
 (i)   PROVED: RS-type rows (finitely many exactly swallowed bad carriers, ANY support profile, (W*), (H2), (H3-inf); no (RR), no (ND')).
 (ii)  PROVED conditionally: infinitely many bad carriers under (W_inf) (rates: rooms, Hoffman constants of growing exact cones, VP
       constants, gaps of bad strict non-peaks).  To make it unconditional one runs the V1/V2 clean-sub-window machinery at the deep-raised
       row; that is item (iii).
 (iii) SKETCH (Theorem M-inf): transport of Master Theorem III' to infinite F.  Flagged inspection items: continuity of the shift-cost rate
       objects (R6) under the deep raise; V1 Lemma ST with the anchor side effects of Lemma TR-inf; V2 Theorem B with the extra pattern rows
       of Lemma W (pinned faces, contact rows on shallow thin targets); window arithmetic.
 (iv)  OPEN residuals specific to infinite F: (NDN) (near-(ND') degeneracy of a on the shallow signature coordinates of carriers that
       need tuning, together with thick support down to the pull depth) and its alternative route "(SC) at companions"; the RS*_inf corner
       case where targets of infinitely many bad carriers cover the initial parts of kernel signature sets (part 4.2(b)); degenerate
       swallowing-sign bad peaks when no donor of the block has a tuning resource (4.3(c)); transported fixed non-d-neutral data (4.1(d),
       not needed).
 (v)   Shared with finite F: (C*) (near-exact coherent shift resonance) and its gap (C*-2) "(SC) at companions"; failure of (H2).
Leaning: positive.  Every infinite-support mechanism examined is either harmless after the deep raise (thin, critical, super-critical,
mu-thin, box-size switching), pinned by the mate's own flip budget (thin shallow coordinates), cushion-dominated ((ND') failure), or a rate
phenomenon of the same "exactness versus scale" type as at finite F.
