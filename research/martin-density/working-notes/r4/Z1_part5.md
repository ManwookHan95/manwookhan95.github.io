# Z1 part 5: the common-functional obstruction at finitely-swallowed points (why exact free resources are not yet enough)

Setting: SLD T, f with F finite, a finite set U* of free carriers closed under slaving (4.3), all other carriers with room (so on every
window sum_{l notin U*} |Delta c_l| <= K t, G3 3.2-3.4 run over l notin U*), and "exact free resources":
 (E1) every l in U* is a strict non-peak of f;  (E2) supp u_l \ F is contained in the contact set K for l in U* (no roomy or near-contact part).
By 4.3, Delta c_{U*} is bounded. Write K_* := union over U* of supp u_l \ F.

## 5.1 What the window decomposition gives. SKETCH (G3 parts 3-4 with U* removed from the pinning system; all estimates as there).
At every window scale t, the + side decomposition splits as
  g = [Cert_+(t)] + [Free_+(t)] + Rem_+(t),
Cert_+(t): G3's balanced finite certificate built from B_+ 1_F and the clamped coarse PINNED carriers (two-sided, valid for |s| <= c_1 t);
Free_+(t): the base part B_+ 1_{K_*} (z-signed, exact contacts) and the U* carrier coefficients c^+_l (strict non-peaks; on the + ray they are
admissible whatever their size, ray lemma 2.3 with Delta1 = 0);
Rem_+(t): base on non-contacts, fine carriers, clamp excess of pinned carriers, normalisations: O(K t) in norm.
Same on the - side with B_- 1_{K_*} (-z-signed). Each "component" Cert_+(t) + Free_+(t) is valid on (0, c_1 t] (one-sided).

## 5.2 The obstruction. PROVED (algebra).
For the windowed averaging (G3 5.2) one needs, at each window scale, a + component and a - component representing the SAME functional
(the + component's functional is Phi_t = g - Rem_+(t)). The - component must use Cert_+(t) (or something within O(K t) two-sided of it), its own
-z-signed base on K_*, and U* carrier coefficients c'_l. Matching the functional forces, on K_*,
  B'_-  =  B_+ 1_{K_*} + sum_{U*} (c^+_l - c'_l) u_l 1_{K_*},
and with c'_l = c^-_l this equals B_- 1_{K_*} + J_t, where J_t := -sum_{l notin U*} Delta c_l u_l 1_{K_*} - (pinned clamp/normalisation terms on K_*)
is O(K t) but has NO sign. B'_- must be -z-signed. Changing c' by xi moves B'_- along span{u_l 1_{K_*}} only. Moving junk between the
sides is impossible: a z-signed addition x on the + side and a -z-signed addition y on the - side change the mismatch by x - y, which lies in
the z-cone; so a mismatch J_t can be cancelled exactly iff -J_t (modulo span{u_l 1_{K_*}}) lies in the z-cone.
Otherwise the wrong-signed part of J_t costs the first-order amount |s| ||J_t^wrong|| <= |s| K t at the scales |s| <= c_1 t where the component
is used, and averaging over the window turns this into |s| K t_1/n (2.4(c)), which is not o(s^2) as s -> 0.
In G3 (no free part) this never arises because the single + certificate is valid on both sides. With free carriers, the two components
differ by an infinite-dimensional, unsigned O(K t) junk on the contact set K_*, and neither G3's averaging nor S3 Theorem D (which needs one
functional, part 3 (O-c)) absorbs it.

## 5.3 Two ways the remaining step could be closed (HEURISTIC; not carried out).
 (a) Make the junk signed: choose, at each window scale, the decompositions (not unique) so that J_t lies in the -z-cone modulo span{u_l 1_{K_*}}.
     Optimal decompositions are only determined up to null pairs (beta, Omega) with beta + L*Omega = 0; it is plausible but not shown that the
     slack rho < 1 (which makes every scale-t decomposition non-tight by (1 - rho^2) t^2/2) leaves enough room for such a choice.
 (b) Engineer the approximant so that the swallowed contact set K_* becomes part of the base support of f' on a window (window masses as in
     P2A/S3 3.3; then contact junk is two-sided there) and lower the far part (3.1); this re-creates the transition band of 3.1(d), now with the
     window-averaged (scale-dependent) data on the band, which is exactly the O3 core localised to the finitely many swallowed signature sets.
