# Z6 referee, part 5: a sharpening of what remains (rigidity is generically lost in mixed blocks at maximal contact)

## Proposition R1. PROVED (under a mild, legitimate design choice on the target sequence).
Design hypothesis (Y+): the target sequence (y^(i)) of Definition SLD contains a countable set Y_+ of NONNEGATIVE vectors of
c_00 ∩ S_{q*} which is dense in {y in c_00 ∩ S_{q*} : y >= 0}.  (Any dense target sequence can be enlarged by such a set;
nothing in Section 8 or in D''' depends on the particular dense sequence.)
Claim.  Let f be at maximal contact (F finite, z ≡ 1 off F; for z ≡ -1 replace "nonnegative" by "nonpositive"), and let
block m contain a bad strict non-peak l^- with q_{l^-} < 0 which is resonant (u_{l^-} >= 0 off F).  Then every
swallowing-type peak p of block m (degenerate or not, any margin) is NON-rigid at all sufficiently large levels.
Proof.  J_- := {j notin F : u_p(j) < 0} is finite (u_p = (y_p + delta_p h_p)/n_p, h_p >= 0, y_p in c_00).  Fix j in J_-.
Choose j' notin F with ||U* e*_{j'}|| < 1/8 (U compact) and put y° := (alpha e*_j + e*_{j'})/q*(alpha e*_j + e*_{j'}) with
alpha > 0 so small that ||U* y°|| < 1/4; then y° >= 0, y°(j) > 0 and y°(zhat) = ||y°||_1 + <U* y°, e> >= 1 - 2||U*y°|| > 1/2
(z ≡ 1 on supp y° and q*(y°) = 1).  By (Y+) there is y in Y_+ with y(j) > 0 and y(zhat) > 1/2 (open conditions).  The target y
recurs infinitely often in block m and is allowed at all large levels (its finite support meets finitely many S_l);
for such a carrier l_j: u_{l_j} = (y + delta h)/n >= 0 off F (resonant at maximal contact) and u_{l_j}(xi) = q0 (y(zhat) +
delta h(zhat))/n > q0/4 for large l_j (delta -> 0, n -> 1), so u_{l_j}(xi) > theta_m Phi_m(k(l_j)) eventually: l_j is a
positive (swallowing-type) peak, q_{l_j} > 0.  Take x_j > 0 with x_j u_{l_j}(j) >= |u_p(j)|.  Put
 nu := e_p + sum_{j in J_-} x_j e_{l_j} + kappa e_{l^-},   kappa := (q_p + sum_j x_j q_{l_j})/|q_{l^-}| > 0.
Then nu >= 0; nu vanishes at anti-sign peaks; u~_p + sum x_j u~_{l_j} >= 0 off F (nonnegative outside J_- ∪ F by definition
of J_-, and on J_- by the choice of x_j) and kappa u~_{l^-} >= 0, so V(nu) is z-signed (K = N \ F at maximal contact): zero
cost; Q_m(nu) = q_p + sum x_j q_{l_j} + kappa q_{l^-} = 0 and Q_{m'}(nu) = 0 for m' != m.  So nu in C_0^+(l) for every
l >= max(p, l^-, l_j) with nu_p = 1.  QED
Consequences.
 (a) At maximal contact (with (Y+)), Theorem V(a) never applies in a compensated block (its compensator l^- is resonant):
     every swallowing-type peak there is non-rigid, so ALL their relative margins enter K_P, and a degenerate positive peak
     in such a block is in the open class (d).  Z6's remark "(a) helps only for non-resonant ones there" is too optimistic
     at maximal contact.
 (b) Conversely (Cor V.1), if block m has no non-rigid q < 0 bad strict non-peak, all its swallowing-type peaks are rigid.
     So at maximal contact the dichotomy is: blocks with a non-rigid q < 0 swallowed non-peak ("negative resources") carry
     non-rigid positive peaks and need margins (rate K_P) and non-degeneracy (else case (d)); blocks without them are rigid
     and need only the rate K_R <= C_f(1 + K_nn).
 (c) Existence of the hard configuration (SKETCH): with |F| >= 2 parameters, "some resonant carrier of block m has
     u(xi) in [-theta Phi, 0)" is open, "some positive peak is degenerate" is a codimension-one condition; both can be met
     simultaneously (intermediate value theorem inside the open set).  Such f are outside every proved class and are the
     sharpest maximal-contact instance of (d).
