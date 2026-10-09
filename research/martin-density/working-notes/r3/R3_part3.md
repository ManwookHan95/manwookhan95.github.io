# R3 part 3: the closure route. Scale-zero closure is trivial (Proposition Z); what a closure theorem would need

## 3.1 Proposition Z (scale-zero closure is trivial). PROVED.
Let f in S_{p*} be such that the free set J = {j notin F : |z_j| < 1} is infinite, and let m_0 in I. For every g in X* with
g(xi) = 0 there are NA functionals f''_n -> f (in norm) and finite certificates c_n at f''_n, supported in block m_0 with
base part 0, such that
  ||g_{c_n} - g||_1 -> 0,   H(c_n) -> 0,   kappa(c_n) = 0   (and r(c_n) > 0).
In particular, for every s_n -> 0 with s_n <= r(c_n): p*(f''_n + s g_{c_n}) <= 1 + o(1) s^2 for |s| <= s_n.
*Proof.* We may assume g != 0. Let x'_N be any NA normer data for approximants of f (e.g. canonical truncations: a'_N :=
truncation of a renormalised, z'_N := z on [1,N] cap {|z_j| < 1} cup supp a'_N with z'_N = sign a'_N there, 0 elsewhere; any
choice with a'_N -> a, z'_N -> z coordinatewise works). Fix d_n -> infinity and r_n -> 0 with r_n <= q*(g)/(4(2+||U||)).
Choose distinct j_{n,1}, ..., j_{n,d_n} in J with sum_l |g_{j_{n,l}}| <= r_n/2 (possible because J is infinite and g in l_1).
G_n := {j_{n,l}}, gamma_n := 1 - max_{G_n}|z_j| > 0. Let zhat_j := z_j + (Ue)_j (so |zhat_j| <= 1 + ||U||) and
  y_{n,i} := g + r_n (e*_{j_{n,i}} - zhat_{j_{n,i}} a),   b_{n,i} := y_{n,i}/q*(y_{n,i}),   eta_{n,l} := e_{j_{n,l}} (unit vector of c_00).
Then y_{n,i}(zhat) = g(zhat) + r_n(zhat_j - zhat_j a(zhat)) = 0 (a(zhat) = 1, g(zhat) = g(xi)/q_0 = 0). Since q*(e*_j - zhat_j a)
<= q*(e*_j) + |zhat_j| <= 2(1 + ||U||) <= 2(2+||U||), we get q*(y_{n,i}) in [q*(g)/2, 2 q*(g)]. Since G_n is disjoint from F = supp a,
y_{n,i}(eta_{n,l}) = g_{j_{n,l}} + r_n delta_{il}, i.e. Y_n := (y_{n,i}(eta_{n,l})) = r_n I + 1 gamma^T with gamma_l := g_{j_{n,l}};
||1 gamma^T||_{inf->inf} = sum_l |gamma_l| <= r_n/2, hence ||Y_n^{-1}||_{inf->inf} <= 2/r_n and, with B_n = diag(1/q*(y_{n,i})) Y_n,
beta_n := ||B_n^{-1}|| <= 4 q*(g)/r_n. Take Pi_n := empty, Phibar_n := 1/n and eps_n := min(gamma_n, 1/n)/(8(2+||U||) d_n beta_n),
so that (iv) of Theorem EC holds. Theorem EC gives f''_n -> f and generic coordinates k_{n,i}. Take c := (q*(y_{n,i})/d_n)_i and
c_n := c''_n(c). Then
  sum_i c_i b_{n,i} = (1/d_n) sum_i y_{n,i} = g + (r_n/d_n) sum_i (e*_{j_{n,i}} - zhat_{j_{n,i}} a),
whose distance to g is <= r_n (2 + ||U||) (as ||.||_1 <= q*), and ||g_{c_n} - sum_i c_i b_{n,i}||_1 <= eps_n ||c||_1 <= 2 eps_n q*(g).
So ||g_{c_n} - g||_1 <= r_n(2 + ||U||) + 2 eps_n q*(g) -> 0. By 2.1(d), H(c_n) <= ||c||_2^2/(m_0^2 C''_n) <= 4 q*(g)^2/(d_n m_0^2 C''_n) -> 0,
because C''_n -> C_{m_0} > 0 (A Fact E along f''_n -> f) and d_n -> infinity; kappa(c_n) = 0. The last statement is A Prop 4.5. QED.
Remark. If J is finite, the same proof with d_n = d fixed (d <= |J|, or using contacts as in 2.2(5)) gives H(c_n) <= 4q*(g)^2/(d m_0^2 C) + o(1).

## 3.2 Consequences for a closure theorem Ls(f) subset K(f)
(a) (PROVED, from Prop Z.) Let K_0(f) be any set defined only through second-order data of approximants at their normers, i.e.
    such that g in K_0(f) whenever g = lim g_{c_n} for certificates c_n at NA approximants f_n -> f with limsup H(c_n) <= 1. Then
    K_0(f) contains the whole hyperplane {g : g(xi) = 0} (when J is infinite). Since every mate vanishes at xi, such a K_0(f)
    contains C(f) and separates nothing. So any closure theorem must use positive scales: the radii r(c_n) of the new
    structure and the distance p*(f_n - f) (equivalently the slack scale).
(b) (HEURISTIC, precise form of what is missing.) The natural multi-scale ingredient would be an IMPLANT INEQUALITY: "at an NA
    f' with eps := p*(f' - f), block coordinates whose status differs between f and f' can carry, two-sidedly at scale t, at most
    C eps/t". (Reason: a coordinate k converted from a peak of f into a non-peak of f' changes w at k by about M, costing
    lambda_k M in L*(w' - w); its two-sided room at scale t is about M lambda_k/t.) Such an inequality is NOT provable for
    admissible T in general: L* is not bounded below, and conversions can be compensated by other status changes (destroyed
    coordinates, base changes, cancellations among near-parallel u_k). It may hold under adversarial assumptions on T
    (e.g. Phi_m(k+1) <= Phi_m(k)/3 plus quantitative independence), but this is not established. OPEN.
(c) (PROVED arithmetic, given (b) as a hypothesis.) Even if an implant inequality holds, it does not exclude carrying O(t)-size
    components at scale t up to t ~ sqrt(eps/kappa): the room lemma 2.3 needs exactly room kappa t^2 <= C eps. Since the slack
    covers t >~ sqrt(eps/(1-rho^2)), an implant-type closure theorem can at best constrain components of g that must be
    carried with size >> t at scales t << sqrt(eps): the O(1) components. For approximate-resonance (O3) mates the switching
    components are carried by f's own structure (matched or converted at the boundary) and only their ERRORS are O(t); so an
    implant-type closure theorem cannot exclude O3 mates whose errors can be carried by EC (i.e. errors with compact
    direction set, part 4). This is why the closure route fails for E's rigid design.
(d) What a valid K(f) would have to encode instead (HEURISTIC): the impossibility of re-creating, near the destruction boundary,
    two-sided carriers of the O(1) switching component at critical rate. By (c) and part 4 this impossibility must come from
    the ESCAPING (non-compact) part of the errors of the boundary carriers, which EC cannot carry (part 5).
