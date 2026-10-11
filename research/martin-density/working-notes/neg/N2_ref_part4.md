# N2 referee, part 4: Section 3 (Lemmas 3.2-3.4, Principle 3.1, Consequence 3.5, designs (A), (B), assessment)

## 4.1 Principle 3.1
 (a) CORRECT (PROVED): f_N := f[a, z 1_{[1,N]}] has a' = a, e' = e, zhat_N - zhat = -z 1_{(N,inf)} for ANY U (the U e terms cancel), so
     u(zhat_N) = u(zhat) - u(z 1_{(N,inf)}) and coordinates in [1,N] keep their status.  (Note: zhat_N equals U e, not 0, beyond N
     unless U e is supported in [1,N].)
 (b) PROVED only at the rows f^# of Section 2 (Lemma 2.2: threshold pinned near 0.8 by the dominant peak); the label "PROVED for
     T_PB" overstates the scope (O2).  In general a quantitative version needs Part II Lemma T(f) and lem:II-T2.
 (c) HEURISTIC, correctly labelled.  What exactly transports is captured by the following PUSH CALCULUS (PROVED here; one block,
     lambda_k = Phi(k), any row with normer direction zhat = z + Ue, zeta^ := R zhat, w = J(zeta^), margins mu^_k in zhat units, so
     |zeta^| |alpha(k)| = lambda_k mu^_k on P by (eq:margin), s_k := sgn w(k)).  Let omega in l_inf with ||D omega||_2 < inf,
     d := <Dw, D omega>/C, g = B + L*(omega - d w).  Then
       (i)   (L*(omega - d w))(zhat) = |zeta^| sum_k omega(k) alpha(k) = sum_{k in P} omega(k) s_k lambda_k mu^_k;
       (ii)  if 1 - td >= 0, C + tdM > 0 and |(1 - td) w(k) + t omega(k)| <= (1 - td) M for all k, then
             N(w + t(omega - d w)) <= 1 + t^2 ||D omega||^2/(2(C + tdM));
       (iii) q*(a + tB) >= (a + tB)(zhat) = 1 + t g(zhat) - t sum_{k in P} omega(k) s_k lambda_k mu^_k.
     Proof.  (i): <omega, zeta^> = |zeta^|(<omega, alpha> + <omega, D^2 w>/C) = |zeta^|(<omega, alpha> + d) and <w, zeta^> = |zeta^|.
     (ii): ||D W||^2 = (C + tdM)^2 + t^2(||D omega||^2 - d^2) for W := (1 - td)w + t omega (expand; (1 - td)C + td = C + tdM), and
     (1 - td)M + C + tdM = 1.  (iii): zhat in B_{q**} and a(zhat) = 1.  QED
     Reading: the l_inf/l_2 part needs NO margin: pushed carriers may be same-sign peaks or strict non-peaks that are not
     near-threshold of the opposite sign (|w(k)| <= (1 - nu)M on the opposite side for pushes of size nu M); the base part pays at
     first order exactly the lambda-weighted margins of the pushed PEAKS (strict non-peaks are free).  So at f_N the decompositions
     of Prop. 2.3-type survive at all scales as soon as the pushed carriers keep their sign or become strict non-peaks, with margins
     at f_N still O(depth) -- e.g. under uniform relative tails |u_k(z 1_{(N,inf)})| <= eta_N Phi(k), eta_N -> 0 -- plus the usual
     first-order correction when g(zhat_N) != 0.  A full inheritance theorem (N2's next step 2) must in addition control the change
     of (M, C, threshold) at f_N and the free-coordinate part of B.  OPEN.

## 4.2 Lemma 3.2 (two-sidedification) -- CORRECT (PROVED)
With U diagonal and e supported in F, U e is supported in F (contained in [1,N]), so zhat_N vanishes on (N,inf) and agrees with zhat
on [1,N]: u_k(zhat_N) = v^near(zhat) = 0.  A peak has zeta(k) = |zeta|(alpha(k) + Phi(k)^2 w(k)/C) != 0 (same signs, second term
nonzero), so k is a strict non-peak with w_N(k) = C zeta_N(k)/(Phi(k)^2 |zeta_N|) = 0, hence d-neutral.  Precision: the hypothesis is
the EXACT equality v^near(zhat) = 0 with the split at the truncation level N itself (for a fixed carrier it applies only for N between
max supp v^near and min supp v^far); approximate versions turn k into a near-threshold carrier, not a two-sided one.

## 4.3 Lemma 3.3 (near free coordinates stay free) -- CORRECT (PROVED)
Part I prop:continuity gives z'_n -> z weak*, i.e. coordinatewise; |z'_n(l)| = 1 on supp a'_n and on contacts.  Valid for any
convergent sequence of rows (NA or not).

## 4.4 Lemma 3.4 (base switching at NA rows) -- CORRECT (PROVED)
G3 Lemma 1.4(c) (refereed) at the normer x' of f': for j notin F', a'_j = 0 and e_j^{+-} >= (1 - |z'_j|) t |B_{+-}(j)|; summing and
using E_b(A_+) + E_b(A_-) <= t^2/q'_0 (G3 Cor. 1.3) gives sum_{j notin F'} (1 - |z'_j|)|V_j| <= t/q'_0.  Since z' in c_0, the room
1 - |z'_j| is bounded below off the finite set F' cup K', so ||V 1_{N \ (F' cup K')}||_1 <= t/(eta_free q'_0).  (Each of B_+ and B_-
separately satisfies the same bound; this is the input of Lemma R2 in part 3.)

## 4.5 Consequence 3.5 -- HEURISTIC (correctly labelled)
It is a classification by exclusion that rests on the heuristic 3.1(c).  Logically: "decided on finitely many coordinates" is
inherited only under the transport conditions of 4.1(c); Lemma 3.2 covers only exactly-zero near values; Lemma 3.4 constrains NA
rows, and at the non-NA row f the analogous statement is G3 Lemma 1.4(c) at f (order-one base switching needs coordinates with
small room, i.e. contacts or near-contacts).  The list (A) base resonances through infinitely many contacts, (B) cancellation
designs, (C) infinite F is a reasonable map of what is left, not a theorem.

## 4.6 Design (B) -- HEURISTIC; one error (C-B1)
 (C-B1) Item (i): "only finitely many pairs can be restored when ||phi_p||_inf <= F_0/delta_0 (spread far parts) ... the adversary must
       spread the far parts" uses the wrong norm and draws the wrong conclusion.  Restoring pair p needs |phi_p(z')| = |phi_p(z)| ~ F_0
       with |phi_p(z')| <= ||phi_p||_1 sup_{supp phi_p} |z'_j|; for infinitely many pairs with supports drifting to infinity and z' in
       c_0 the sup tends to 0, so infinitely many restorations are impossible as soon as sup_p ||phi_p||_1 < infinity -- which is
       AUTOMATIC when the normalisations n_p are bounded (q*(u) = 1).  The l_inf-size (spreading) is irrelevant.  So restoration is
       never the answer for infinitely many pairs, whatever the adversary does; the discussion correctly moves on to (ii) shared far
       parts and (iii) crossing conversions.  No downstream effect.
 (iii) crossing conversions: plausible at model level; precision: the converted pair is used LINEARLY (two-sided), so its far
       error cannot be "banked" on contacts (a contact is one-sided: on the side where z'_j B_j < 0 it costs 2t|B_j| at first order); it
       must be banked on support coordinates (tiny masses of a'), with the window depending on the scale.  This is the standard
       engineering of Rounds 2-8; not re-verified here.
 (iv)-(vi): HEURISTIC, consistent with r1/E_notes 7.3 (rigid design) and the (LIN) formulation; (LIN) is new and is a reasonable
       linear necessary condition, but nothing about it is proved.

## 4.7 Design (A) -- status summary CONSISTENT with the refereed record
(d-neutral exact resonances recovered for every admissible T; Delta d >= 0 under (TC); Delta d < 0 under (SC)/(PC*); without (SC) and
rho near 1 OPEN).  The remarks on non-canonical truncations and outward-moving resonances are SKETCH/OPEN as labelled.

## 4.8 Assessment 3.4/3.6 and the answer of Section 0
 * "A non-recovery proof needs a uniform lower bound over all NA approximants" -- CORRECT (Remark 1.3 as proved in part 1), but the
   tool proposed for it must be Lemma 1.4'' (balanced), not the per-carrier reading (F2).
 * "No technique for such statements exists in the sources" -- accurate description of the record.
 * "The adversarial choice of T alone does not create obstructions" and "every explicit adversarial mechanism has a recovering
   approximant family" -- OPINIONS supported by examples, not theorems (direction (b) of the referee brief: a claim that no
   obstruction can exist must be proved; N2 does not claim to prove it, and its table lists non-recovery as OPEN).  The phrase
   "the canonical truncations recover everything" must be weakened (O1).
 * "Leaning: POSITIVE" -- a judgement; the referee agrees that nothing in N2 or in Rounds 1-14 points to a counterexample, and that
   the negative route is not easier, but notes that the example of Section 2 is far from the actual open core of the positive
   program (ADDENDA 13-14: pinned wrong-signed strict minors with escapes, (LSC-trunc) at infinite F), so it is evidence about
   mechanisms, not about the residual rows.
