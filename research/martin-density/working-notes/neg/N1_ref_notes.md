# N1 referee notes: proofs of the fixes and additions

Companion to neg/N1_referee.md. Part files: neg/N1_ref_part1.md (Section 1 and Lemma 2.1 of N1), neg/N1_ref_part2.md
(Sections 2-4 of N1). Scripts: neg/N1_ref_work/ref_checks.py, neg/N1_ref_work/rerun_R3_capacity.sh.
Setting and notation as in N1_notes.md Section 1: any admissible T, any nonempty block set I (finite where a cited result
needs it), X = c_0 with p, S* = S_{p*}, NA_1 = grad p(S_p), C(f) the mate fibre, r~_f its support function on X,
Rec(f) the outer limit of C along NA rows, A(f) the Hausdorff cluster sets of C along NA sequences, U(f) the inner limit
along all sequences, Omega the comeager set of continuity points of C. "[I, label]" = Part I.
Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.

## 1. Two-sided far freedom

LEMMA 1.4' (converse of N1 Lemma 1.4).  PROVED.  Let f in S* have forced data (a, z). For every eta > 0 and W in N there is
delta_0 > 0 such that every f' in NA_1 with p*(f' - f) < delta_0 has forced data (a', z') (a' = grad q(x'), z' = x'/q(x') -
U(U*a'/||U*a'||), x' the normer of f') with ||a' - a||_1 < eta and |z'_j - z_j| < eta for every j <= W.
Proof. If not, there are eta, W and f'_n in NA_1 with p*(f'_n - f) < 1/n violating the conclusion. By [I, prop:approximants]
(i)=>(ii) (which rests on [I, prop:continuity]: a_n -> a in l_1 and z_n -> z weak*, and for an NA row the bidual normer is the
normer x'_n, so z_n = x'_n/q(x'_n) - U e_n = z'_n), a'_n -> a in l_1 and z'_n -> z coordinatewise; for large n both
conditions hold. Contradiction. QED
Together with N1 Lemma 1.4: the NA rows near f are EXACTLY the rows grad p(z' + U(U*a'/||U*a'||)), a' in c_00 cap S_{q*},
z' in B_{c_0}, z' = sgn a' on supp a', with (a', z') close to (a, z) in l_1 x (coordinatewise on a window).

COROLLARY 1.4'' (where banks can sit).  PROVED.  Let j be a coordinate.
 (a) If j is a free coordinate of f (j notin F, |z_j| < 1), there is delta_j > 0 such that no f' in NA_1 cap B(f, delta_j)
     has j in supp a'.
 (b) If j in F u K, every f' in NA_1 close enough to f with j in supp a' has sgn a'_j = z_j (contact sign / support sign).
Proof. Apply Lemma 1.4' with W = j and eta < 1 - |z_j| (case (a)) or eta < 1 (case (b)); on supp a', z'_j = sgn a'_j = +-1,
which must lie within eta of z_j. QED
So near f, banks at fixed positions live on contacts (with the contact sign) or near-contacts; sign-flipped masses ("far
pulls") and banks at free coordinates must escape to infinity as f' -> f. N1's "tiny banks anywhere" holds only beyond the
window.
Application to [II, prop:II-S3] (the only known lower-bound mechanism; it is a type (I) obstruction with the two-point test
vector x = psi(s_2) e_{s_1} - psi(s_1) e_{s_2} in c_00, valid along rows whose mates carry two-piece data and whose set
Sigma_n avoids s_1, s_2). If s_1, s_2 are FREE coordinates of f, Cor 1.4''(a) shows that NA rows near f cannot put s_1 or
s_2 into their base support (no support coordinate, no bank there); the only escape left to them is to cover s_1 or s_2 by
the support of a strict non-peak (or to leave the two-piece class). This sharpens the remark after [II, prop:II-S3]; the
carrier escape itself remains available for every admissible T (dense tails of (u_{k,m})_k, zero-weight non-peaks created by
o(1) far moves, R3 Theorem EC).

## 2. Localization of type (I) obstructions

For f in S* and x in X put h_f(x) := sup_{g in Rec(f)} g(x) (= limsup_{NA_1 ∋ f' -> f} r~_{f'}(x), N1 Thm 1.9(a)) and
Delta_f(x) := r~_f(x) - h_f(x) >= 0. Let D_f be the set of Gateaux-differentiability points of r~_f (a dense G_delta of X by
Mazur's theorem).

LEMMA R-I.  PROVED.
 (a) Delta_f is even, positively homogeneous and 2p-Lipschitz.
 (b) O_f := {x in X : Delta_f(x) > 0} is an open symmetric cone. f carries a type (I) obstruction (N1 Thm 1.9(d)) iff
     O_f is nonempty; then O_f meets c_00 and D_f, and for x in O_f cap D_f the unique maximizer g_x of x on C(f) is an
     X-exposed mate with g_x notin Rec(f).
 (c) If Delta_f(x) >= 3 theta > 0, there is delta > 0 such that r~_{f''}(x) <= r~_f(x) - 2 theta for EVERY recoverable row
     f'' in B(f, delta) (Rec(f'') = C(f''); e.g. f'' in NA_1 or in Omega), and the set
     Z := {f'' in S* : p*(f'' - f) <= delta/2, r~_{f''}(x) >= r~_f(x) - theta} is closed, contains f, and is nowhere dense in S*.
Proof. (a) Rec(f) and C(f) are symmetric subsets of B_{p*} (p*(g) <= 1 on C(f), [I, prop:reduction(c)]); support functions of
such sets are even, 1-homogeneous and p-Lipschitz. (b) Openness from (a); O_f nonempty iff h_f != r~_f somewhere iff (b2) of
N1 Thm 1.9 fails iff (I). A nonempty open set meets the dense sets c_00 and D_f. At x in D_f the subdifferential of the
support function r~_f is the face {g in C(f) : g(x) = r~_f(x)} (N1 Thm 1.9 proof), a singleton {g_x}; if g_x were in Rec(f)
then h_f(x) >= g_x(x) = r~_f(x). (c) Choose delta with r~_{f'}(x) <= r~_f(x) - 2 theta for all f' in NA_1 cap B(f, delta)
(possible because limsup_{NA_1 ∋ f' -> f} r~_{f'}(x) = h_f(x) <= r~_f(x) - 3 theta). If f'' in B(f, delta) is recoverable,
N1 Thm 1.9(a) at f'' gives r~_{f''}(x) = h_{f''}(x) = limsup_{NA_1 ∋ f' -> f''} r~_{f'}(x), and NA rows close to f'' lie in
B(f, delta); hence r~_{f''}(x) <= r~_f(x) - 2 theta. Z is closed because f'' -> r~_{f''}(x) is upper semicontinuous
([I, thm:compact]); f in Z; Z contains no recoverable row, in particular Z cap Omega is empty, and Omega is dense, so Z has
empty interior. QED
Reading. A type (I) obstruction is a "ridge": in a fixed direction x in c_00 the scalar usc function f'' -> r~_{f''}(x) is
>= r~_f(x) - theta on a closed nowhere dense set through f and <= r~_f(x) - 2 theta on every recoverable row nearby.

## 3. Merging and convexity of Rec(f)

LEMMA R-M.  PROVED.  For f in S* the following are equivalent:
 (alpha) Rec(f) in A(f), i.e. some NA sequence f_n -> f has C(f_n) -> Rec(f) in the Hausdorff metric;
 (beta)  (finite merging) for all g_1, ..., g_k in Rec(f) and eps > 0 there is f' in NA_1 with p*(f' - f) < eps and
         max_i dist(g_i, C(f')) < eps.
If they hold, Rec(f) is convex, so f carries no type (II) obstruction, and then Rec(f) = C(f) iff Delta_f = 0.
Moreover [I, cor:finite(a)] at f ("C(f) subset Li_n C(f_n) along one NA sequence") holds iff C(f) in A(f), i.e. iff
Rec(f) = C(f) and (alpha) holds.
Proof. (alpha)=>(beta): if C(f_n) -> Rec(f) in the Hausdorff metric, every g_i in Rec(f) satisfies dist(g_i, C(f_n)) <=
d_H(C(f_n), Rec(f)) -> 0. (beta)=>(alpha): Rec(f) is compact; let N_n be a finite (1/n)-net of Rec(f) and choose by (beta)
f_n in NA_1 with p*(f_n - f) < 1/n and dist(h, C(f_n)) < 1/n for h in N_n. By Blaschke (all C(f_n) lie in a fixed compact set,
[I, thm:compact]) a subsequence satisfies C(f_n) -> A in A(f). For g in Rec(f) pick h in N_n with p*(g - h) <= 1/n; then
dist(g, C(f_n)) < 2/n, so g in A. Thus Rec(f) subset A subset Rec(f) (N1 Prop 1.2(b)). Every A in A(f) is convex (N1 Prop
1.2(b)), so (alpha) gives convexity, and then N1 Thm 1.9(b) gives Rec(f) = cl conv Rec(f) = C(f) iff (b2) iff Delta_f = 0.
Last claim: if C(f) subset Li C(f_n) for an NA sequence, any Hausdorff cluster set A of (C(f_n)) contains C(f) and is
contained in C(f), so C(f) = A in A(f), and then Rec(f) = C(f) (A subset Rec(f) subset C(f)); conversely C(f) =
lim_H C(f_n) gives C(f) subset Li C(f_n). QED
Consequences. (1) The gap noted at the end of [I, sec:status] (does density force [I, cor:finite(a)]?) is exactly: does density
force finite merging at every f? (2) N1's type (II) is one way finite merging can fail (non-convex Rec(f) cannot be a single
A); it is not "the precise form" of that gap (correction P-12). (3) A positive programme may be split as N1 suggests, with
(P-II) stated as finite merging (beta); then density <=> (P-I) (Delta_f = 0 for all f).

## 4. Precise form of M2

PROPOSITION R-M2.  PROVED.  Let I be finite, g in C(f) with g notin Rec(f). For all c_0 > 0 and kappa_1, K < infinity there
are eta > 0 and arbitrarily small t > 0 such that for NEITHER tau = t NOR tau = -t is there a finite certificate
c_t = (b_t, omega_t) at f with r(c_t) >= c_0 t, kappa(c_t) <= kappa_1 and e_t := g - g_{c_t} with p*(e_t) <= K t such that the
decomposition f + tau g = (a + tau b_t + tau e_t) + sum_m R_m^*((1 - d_{t,m} tau) w_m + tau omega_{t,m}) has all component
norms <= s(tau) + eta tau^2.
Proof. For t > 0 let A(t) in [-infinity, infinity] be the infimum, over all such certificates and both signs of tau, of
max(component norms) - s(tau) (A(t) = +infinity if no certificate with the radius, kappa and error bounds exists). If
limsup_{t -> 0+} A(t)/t^2 <= 0, choose for each small t a certificate and a sign with excess <= max(A(t), 0) + t^3; the
excesses are o(t^2), so the hypotheses of [I, cor:decomposition] hold (I finite, so its extra hypothesis is automatic) and
g in cl Cert(f) subset U(f) subset Rec(f) (cl Cert(f) is recovered along every sequence by [I, thm:transport] / [I, cor:lsc]).
Hence limsup A(t)/t^2 > 0; any eta below half of it works. QED
(The same applies to rho g in place of g, rho g being an element of C(f) outside Rec(f) for the rho of a counterexample.)

## 5. Corrected form of M4/M6 (error E-1)

PROPOSITION R-E1.  PROVED (contrapositive of [I, thm:engineered]).  Let I and F be finite, g in C(f) and rho in (0,1) with
rho g notin Rec(f). Then exactly one of the following holds:
 (i)  g carries no two-piece data (b^+-, omega^+-) with rho^2 kappa_w < 1;
 (ii) g carries such data, and for EVERY such datum the block set I_- = {m : Delta d_m < 0} fails (SC) (in particular
      I_- is nonempty, f is not (BT), and the datum's switching vector v := b^+ - b^- is exact (scale-free), nonzero,
      supported in F u K with z_j v_j >= 0 on K, and has infinitely many contacts in its support).
Proof. If some datum with rho^2 kappa_w < 1 had I_- empty or satisfying (SC), [I, thm:engineered] would give
(f, rho g) in cl NA, i.e. rho g in Rec(f) (N1 Prop 1.2(d)). (BT) implies (SC) for every block set (remark after
[I, def:SC]). Since both pairs represent g, v = b^+ - b^- = L*X with X_m := (omega^-_m - omega^+_m) - Delta d_m w_m
(the sandwich identity of [II, cor:II-S2]); if v = 0 then X = 0 (L* injective), so omega^-_m - omega^+_m = Delta d_m w_m,
and evaluating on the nonempty peak set P_m (where omega^+-_m vanish and |w_m| = M_m > 0) gives Delta d_m = 0 for all m,
contradicting I_- nonempty. So v in Y \ {0}, hence v is not finitely supported ((T-c)). Side admissibility gives
v_j = 0 off F u K and z_j v_j = z_j b^+_j - z_j b^-_j >= 0 on K; F being finite, supp v contains infinitely many
contacts. QED
So the switching of a dangerous mate is "genuinely scale-dependent or not of two-piece type" ONLY in case (i). Case (ii) is
exactly N1's own candidate C1. The gloss after M4 ("its one-sided decompositions need infinitely many carriers, degenerate or
near-threshold carriers, or flips of an infinite support") likewise holds only in case (i): in case (ii) the carriers of g
are finitely many and the failure of (BT) is used through the SCRAMBLING of the block (deep zero-weight or near-threshold
carriers of f), not through g's own decomposition.

## 6. Error E-2: the refereed status of R3 (error carrying) and the capacity route (R6)

Fact (from r3/R3_referee.md, "Main finding", and r3/R3_ref_part3.md; reproduced here): R3's Theorem EC (PROVED, any
admissible T) removes the ERROR-driven conversion requirement at a junction, but not a rho-independent HILBERT/ROOM
capacity requirement: below the band the O(1) switching component must be carried by converted carriers with block
coefficient rho^2 S^2/(N m_0^2 C''), so (HC) needs N >= rho^2 S^2/(m_0^2 C'' Q) converted carriers, and above the band
the room ~ 4 M lambda_b/t of the destroyed carriers must be replaced.
Reproduction (N1_ref_work/rerun_R3_capacity.sh, scripts of r3/refwork, Model N, a_0 = 0.03, delta = 1):
 - one type converted (one shift), EC: A = 0.5: R = 1.091; A = 0.25: R = 1.447; maximum at the bottom scale tau = 2^-8,
   identical for tau_gen = 2^6 and 2^8 (bottom value B S^2/n_conv exceeds sup P_f);
 - coupled (real-norm-like) model, A = 0.1 delta: one shift R = 1.0901 (boundary layer, tau ~ 4.5); two shifts R = 0.9998.
(The R3 referee's own runs give 1.463 / 2.074 and 1.090 / 1.0000 under its parameter choices; the qualitative finding is the
same.) Hence:
 - N1 (T2): (R1) "escaping errors" is NOT necessary even heuristically; O3* must read [(R1)-(R5)] OR (R6) (conversion capacity
   of at least one type below the Hilbert/room load at every junction, all errors compact).
 - N1 3.3(iv): delete "So the obstruction must ALSO make the errors at every junction escape to infinity (non-compact)".
 - N1 (Q-a): E's rigid design is NOT shown recovered (SKETCH with two gaps: (HT-EC) and the capacity gap).
Status of (R6): OPEN. In every coupled model tested, converting both types (two group scalars) suffices; whether an
admissible T can block two-type conversion at every junction is open. This is the only route where refereed model-level
evidence exhibits a junction-depth-independent deficit of a concrete mechanism.

## 7. Remarks on candidate C1 (HEURISTIC, with one PROVED identity)

(e5) Footprint compensation. IDENTITY (PROVED): let a' in c_00 cap S_{q*}, e' := U*a'/||U*a'||, and let e^0 be any unit vector of
H. For every z' in B_{c_0} with z' = sgn a' on supp a', the vector z'' := z' - (U(e' - e^0)) 1_J, where J is a finite set of
coordinates outside supp a' with |z'_j - (U(e' - e^0))_j| <= 1 on J, again satisfies z'' in B_{c_0}, z'' = sgn a' on supp a',
hence (by [I, prop:smooth(c)]) y'' := z'' + U e' has q(y'') = 1 and grad q(y'') = a', and y''_j = z'_j + (U e^0)_j for j in J.
So the Hilbert footprint U(e' - e^0) of window masses can be removed exactly on any finite set of free coordinates (and, inward
only, on contacts); by Lemma 1.4 the modified row is still close to f when ||U(e' - e^0)||_inf is small. What cannot be removed
is the footprint on supp a' (F and the banked window contacts) and on contacts needing an outward move. HEURISTIC consequence:
the C1 scrambling mechanism (N1 3.4) needs zero-weight carriers whose vectors carry O(1) relative mass on F u K at every depth.
(e6) Non-uniqueness of data: C1 must be in case (ii) of Proposition R-E1 for EVERY datum with rho^2 kappa_w < 1.
(e2') Since ||U*e_j*|| -> 0 for every compact U, only the footprint of the COARSE window contacts (fixed by g) can be made large
by the choice of U.

## 8. What remains open (precise)
 1. Existence of (T admissible, N, f, g in C(f)) with g notin Rec(f) (non-density of NA((c_0,p_N), l_2^2)). OPEN.
 2. Type (I): some (T, f, x in c_00) with Delta_f(x) > 0 (Lemma R-I). OPEN. Type (II): non-convex Rec(f). OPEN.
 3. Positive counterparts: (P-I) Delta_f = 0 for all f; (P-II) finite merging (Lemma R-M (beta)) for all f. Both OPEN; their
    conjunction is equivalent to density plus [I, cor:finite(a)] at every f.
 4. Candidate C1 (case (ii) of R-E1 with (SC) failing): existence of T, f, g not constructed; escapes (e1)-(e6) not closed. OPEN.
 5. Capacity route (R6): whether an admissible T can force, at every junction of every NA approximant, a Hilbert/room load above
    the available two-type conversion capacity. OPEN (model evidence: two shifts suffice in all coupled tests).
 6. (N-a) mates with genuinely scale-dependent switching at all scales (case (i) of R-E1) at some row: not constructed;
    (N-b) any lower bound for dist(rho g, C(f')) over ALL NA rows f' near some f: none known. OPEN.
 7. For the designed T_fin: (LSC-trunc)_N (equivalent to density for p_N by Part III). OPEN.
