# Q1 referee (a) — part 4: the constants that are NOT absolute (window bookkeeping) and the fix (working file)

## H. Where level-dependent exponents enter (re-derived from U1 2.3-2.4, V2 Lemma H)
H1 Class thresholds (U1 2.3): A_1 := K_*, A_{i+1} := K_* A_i (i <= J + 1), J := |Omega| + N <= L + N.  The class of a scale is read off
   the projected data; components below A_{i(t)} K t are zeroed at cost <= J A_{i(t)} K t <= J K_*^{J+1} K t.  So the constant of (E-c) is
   K_data <= J K_*^{J+1} K with K_* = C_f (Design/u)^{C}: its exponent grows LINEARLY in L + N, and C_f appears to the power J.
H2 Cube count (U1 2.4(c)-(d)): (A_max/eps)^p with p = number of extreme rays of Gamma^#(kappa, a) (a design number growing with L) and
   eps <= c/(C_f p) (so that the - side Gamma grows by <= C_f p eps).  Exponent p, f-constant to the power p.
H3 Q1 (S6) states D_cls(w) <= C_{f,N} (Design/u)^{C_D} and K = C_f (Design/u)^{C_K} with ABSOLUTE C_D, C_K, and Theorem C^tr's (E-d) uses
   C_U1 - 2 C_D = C_K + 1.  This bookkeeping is wrong as stated (it is inherited from U1/U1-ref, which wrote "(Design/u)^{C}" without
   tracking J and p).  The conclusion survives because Q(w) also contains (4 Design(l)/u(w))^{omega(l) + 20} and omega(l) (the number of
   rate objects of level l, which includes the minors of Gamma^#(kappa, a) for every pattern kappa and class a of level l) is at least the
   number of patterns, >= 2^l; but this has to be said, and p must be controlled.

## I. Fix (PROVED)
I1 Refined pigeonhole (replaces U1 2.4(c)-(d) in MT VI Step 2).  For each scale t choose (fixed rule) a basic representation
   Delta'(t) = sum_{j in J(t)} a_j(t) g_j with |J(t)| <= N, g_{J(t)} linearly independent, a_j(t) >= 0 (Caratheodory).  Pigeonhole over
   the support J(t) (<= (p + 1)^N choices) and then over eps-cubes of [0, A_max]^{J(t)} (<= (A_max/eps + 1)^N cubes).  For a set S of
   scales with one support J and one cube with corner a^max put Delta'^* := sum_{j in J} a^max_j g_j, incr(t) := sum_{j in J}
   (a^max_j - a_j(t)) r_j.  Then incr(t) is a nonnegative combination of extreme rays, hence in Gamma^#(kappa, a);
   Delta'(t) + Delta'(incr(t)) = Delta'^*; ||incr(t)||_1 <= N eps.  Everything else of U1 2.4(e) is unchanged (the - side grows by
   C_f N eps in sqrt Gamma, so eps := c_f (u/Design)^C/N suffices).  Count:
       D_cls(w) <= (J + 1) 3^J (p_max(L) + 1)^N (A_max/eps + 1)^N <= C_{f,N} 3^{2L} (p_max(L) + 1)^N (Design(L)/u(w))^{2 C N}.
I2 Window exponent.  Put p_max(L) (the largest number of extreme rays over the patterns and classes of level L, a design number) into
   Design(L) and use Q(w) := (4 Design(l)/u(w))^{omega(l) + l^2 + 20} (or keep Q1's Q(w) and prove omega(l) >= l^2: omega(l) >= number of
   patterns >= 2^l).  Then for L >= l_f(f, N):
       log_{4 Design/u} [ D_cls(w)^2 K_data(w) / (c_flat(w) C_{f,N}^2) ] <= C (L + N) + 2 N + 4 C N + 2 L + C <= L^2 + 20,
   since C_f <= Design(L)/u for L large (Design(L) -> infinity), J <= L + N, 3^{2L} <= Design(L), p_max <= Design(L).  Hence
   |S| c_flat/K_data >= n(w)/(D_cls^2 K_data/c_flat) >= L 2^{L^3} -> infinity and K_data T_hi(w)/|S| <= 2^{-L^3} -> 0: (E-d) holds.
   Q only grows, so U4's Lemma GW and every window condition remain valid (monotone in Q).  NO other part of T_fin changes.
I3 With I1-I2, Theorem C^tr and MT VI(a) are PROVED modulo the refereed tools (as Q1 claims), for L >= l_f(f, N, g, rho).
