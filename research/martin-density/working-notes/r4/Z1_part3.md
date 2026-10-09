# Z1 part 3: the referee's route, quantified; a better family of approximants; where the proof stops

Standing: SLD T, p = p_N, f in S_{p*} with F finite, g in C(f) NOT window-pinned (otherwise Theorem B* applies), rho < 1.
Design adjustment (harmless): choose the signature sets in (D0) with m_l := min S_l STRICTLY INCREASING in l (e.g. S_l := {2^l(2i+1) : i >= 0}
minus j_0). G3's Theorem A uses only that the S_l are pairwise disjoint infinite subsets of N \ {j_0}; Theorems B, C use nothing else about
the S_l. So A-C remain valid verbatim (PROVED by inspection).

## 3.1 What the far lowering of a swallowed set does (referee's route). PROVED parts / HEURISTIC parts marked.
Let l_0 be a swallowed carrier (S_{l_0} contained, up to finitely many points, in contacts or near-contacts of f), n large, gamma in (0,1), and
f'_n given by (a, z'_n) with z'_n := (1 - gamma) z on G_n := S_{l_0} cap (n, inf), z'_n := z elsewhere (1.1(a)).
 (a) PROVED. f'_n -> f; the room of S_{l_0} at f'_n is ||h_{l_0} 1_{G_n}|| / ||h_{l_0}|| <= 2^{m_{l_0} - n} -> 0, so the pinning constant of
     l_0 at f'_n is delta'_{l_0}(n) <= delta°_{l_0} 2^{m_{l_0}-n}, and G3 3.2 at f'_n gives |Delta c_{l_0}| <= (t/(gamma q_0') + finer)/delta'_{l_0}(n):
     at f'_n the carrier l_0 is effectively pinned only at scales t <~ theta_n := gamma delta'_{l_0}(n) |Delta c|, i.e. below ~ 2^{-n}.
 (b) PROVED (G3 2.3(b) at f'_n). A switching of size |Delta c_{l_0}| through l_0 at scale t costs at f'_n the first-order amount
     gamma t |Delta c_{l_0}| delta'_{l_0}(n) (signature mass on the lowered part), so switching of size O(1) is affordable at f'_n exactly
     for t >~ theta_n.
 (c) HEURISTIC (cannot be proved for general T: L* is not bounded below, R3 3.2(b)). Generically eps_n := p*(f'_n - f) is of order
     min(lambda_{l_0}, gamma delta'_{l_0}(n)) ~ theta_n: by Fact C, if k_{l_0} is a strict non-peak of f, w'(k_{l_0}) - w(k_{l_0}) =
     C m u_{l_0}(xi'_n - xi)/(Phi |zeta|) + o, i.e. lambda_{l_0} |w' - w|(k_{l_0}) ~ C m^2 |u_{l_0}(xi'_n - xi)|/|zeta| ~ gamma delta'_{l_0}(n).
 (d) Consequence (PROVED as arithmetic from (a)-(c)). The slack of rho < 1 covers |tau| >~ sqrt(eps_n/(1 - rho^2)) ~ sqrt(theta_n), the
     pinning of f'_n starts below theta_n, so there is a TRANSITION BAND [theta_n, sqrt(theta_n)] (ratio -> infinity) on which f'_n must
     reproduce f's switching through l_0 with o(tau^2) error, while the trivial transfer costs eps_n >> tau^2 there. Lowering MORE
     (gamma larger, or on a larger part of S_{l_0}) only moves the band; it cannot be removed. So the band needs an EXACT transfer
     (as in P2A Thm 2.1: decompositions recomputed at f'_n, d-coefficients re-solved, steering). This is where the proof stops (3.4).

## 3.2 Better approximants: lower whole FINE signature sets, keep the coarse ones. PROVED.
For L in N let n_L := m_{L+1} - 1 and define f^L by (a, z^L) with z^L_j := 0 for j in S_l, l > L, and z^L_j := z_j otherwise.
 (a) f^L -> f as L -> infinity (z^L differs from z only on [m_{L+1}, inf); 1.1(a)).
 (b) Every S_l with l > L is entirely roomy at f^L (z^L = 0 there, and S_l misses the finite F for L large), with pinning constant
     delta'_l = delta°_l (full mass, gamma = 1/2); every S_l with l <= L keeps exactly the room it had at f. Hence f^L in R_0 iff the
     finitely many coarse sets S_1..S_L have room at f; in general f^L lies in
        R_fin := {f in S_{p*} : F finite, and (SR) holds for all l > L, for some L}  ("finitely swallowed points").
 (c) Coarse data are kept: for l <= L the vector u_l vanishes on the modified coordinates (its signature is on S_l, and by allowedness (a)
     its target y_l misses S_{l'} for l' >= l; for l' > L >= l this is the case), so u_l(zhat^L) = u_l(zhat); the forced data of f^L on coarse
     carriers differ from those of f only through the normalisations q_0, |zeta_m|, C_m, M_m, which converge (P2A Lemma 1.2 / G3_ref 3.3).
 (d) Fine carriers at f are box-bounded: for every two-sided decomposition at scale t, sum_{l > L} |Delta c_l| <= 6 sum_{l>L} lambda_l / t
     <= 6 c_{L+1}/t (G3 3.1, (P2)). So at scales t >> sqrt(c_{L+1}) the switching of g through ALL fine carriers is o(t), i.e. g is "pinned
     modulo the coarse swallowed carriers" there.
So, compared with 3.1, the transition band attached to the fine carriers sits at scales <~ sqrt(c_{L+1}), where these carriers are only
box-bounded (amplitude <= 6 lambda_l/t), and the coarse swallowed carriers are not touched at all.

## 3.3 Reduction. PROVED.
Let R_fin be as in 3.2(b). If (A) R_fin is contained in R and (B) for every f with F finite, g in C(f), rho < 1 there are f' in R_fin
arbitrarily close to f with dist(rho g, C(f')) -> 0, then NA((c_0,p_N), l_2^2) is dense (for F infinite see part 4).
*Proof.* As G3 5.4 (<=) with R_0 replaced by R_fin and Theorem B replaced by (A). QED.
Status: (A) is G3 6.3(d) (finitely many unpinned carriers, plus coarser carriers slaved to them, G3_ref 5): OPEN. (B) along f^L is OPEN.
Neither is implied by the other; both are strictly weaker than the original Lemma Z only in bookkeeping, not in kind.

## 3.4 The precise obstruction (what a proof of Lemma Z must still supply). SKETCH (the split) / PROVED (the arithmetic) / OPEN (the step).
Fix a window W(l_*) of f (l_* >= L). Exactly as in G3 parts 3-4, but declaring the carriers l <= l_* with room < vartheta^l at level gamma
(and those slaved to them) FREE, every two-sided decomposition at a window scale t splits as
   g = Cert(t) + Free_+(t) + Rem_+(t) = Cert(t) + Free_-(t) + Rem_-(t),
where Cert(t) is the (+ side) balanced finite window certificate (valid two-sidedly for |s| <= c_1 t, G3 5.1), Rem_+-(t) = O(K t) in norm
(K = K_1 vartheta^{-l_*^2} Lambda°(l_*)), and Free_+-(t) are the one-sided parts carried by the free carriers and their base counterparts
(signature mass on the swallowed sets, target mass), with Free_+(t) - Free_-(t) = O(K t) AS FUNCTIONALS but O(1) as decompositions.
Two independent defects remain:
 (O-a) NEAR resources in Free (near-contacts on swallowed sets, weak peaks among free carriers): Delta1 > 0, so by the ray lemma (2.3, 2.4(b))
       the one-sided part Free_+(t) is usable only on [c Delta1(t), t]: genuinely scale-dependent switching (O3 localised to signature sets).
 (O-b) Even with EXACT free resources (Delta1 = 0 on Free, so each side is a valid one-sided linear decomposition on the whole ray, 2.4(a)),
       averaging over the window yields two ONE-SIDED objects ghat_+ = avg(Cert + Free_+), ghat_- = avg(Cert + Free_-) with
       ||ghat_+ - ghat_-|| <= 2 K t_1/n, NOT one functional. At scales |s| < c K t_1/n the mismatch costs first order |s| K t_1/n
       (2.4(c)); it is a FIXED vector (not O(scale)), so R3's error carrying (EC + room lemma, which needs errors of size O(scale)) does not
       apply, and P2A/S3's steering removes only finitely many scalar mismatches (d-coefficients), not an infinite-dimensional remainder.
 (O-c) Why the obvious combination "window averaging (G3 5.2) + engineered two-piece recovery (S3 Thm D)" does not close (O-b). PROVED
       (arithmetic). S3 Thm D tolerates a mismatch e between the two side data if 2 rho ||e|| <= eps_0 s_1 (e enters only the side pieces, used
       for |tau| > s_1, as a genuine first-order cost 2 rho |tau| ||e||; the theta-piece used for |tau| <= s_1 represents g' exactly). But
       (i) the averaged block data have coordinatewise radius r ~ c_1 t_1 2^{-n} (bottom of the window), so the slack at f' is usable only if
           p*(f' - f) <~ (1 - rho^2) r^2, and Thm D's approximants have p*(f' - f) >~ s_1 (window masses 4 rho s_1 |b^theta_j|);
       (ii) the mismatch is eta ~ K t_1/n.
       Hence one needs K t_1/(n eps_0) <~ s_1 <~ t_1^2 4^{-n}, impossible since 4^{-n} << K/n. Equivalently: G3's averaging pays its O(K t_i)
       errors with the slack AT f at scales >= c_1 t_i, but at an engineered f' the slack starts only at sqrt(p*(f'-f)) >> bottom of the window.
       G3 escapes this because its averaged object is a single TWO-SIDED certificate, which transports to any f' with no error (A Transport
       Theorem / C Thm 7.4). With free carriers, two DIFFERENT one-sided objects are unavoidable on every window.
REMAINING STEP (OPEN, stated precisely): "two-piece closing with small mismatch": for f with F finite and one-sided exact-resource data
(Cert, Free_+, Free_-) as above with mismatch e := avg(Rem_- - Rem_+), ||e|| <= eta, show that rho ghat_+ is within o_eta(1) of C(f') for some
f' in R_0 near f (or of Ls(f)), uniformly as eta -> 0 along the windows; together with a treatment of (O-a).
