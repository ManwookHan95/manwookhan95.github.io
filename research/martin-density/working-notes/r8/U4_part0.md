# U4 part 0 — reading digest (design features used by refereed Rounds 5-7 results)

Sources read: BRIEFING, BRIEFING_R2 (Addenda 1-7), martin_paper_summary, note Sec 1 (def:admissible, lem:martintail),
Sec 8 (def:SLD, thm:SLD, R_0, windows, thm:R0, thm:reductionZ, rem:lemmaZ), r7 referee reports V1-V4, V1 head/part1/2/3/4,
V2 head/Part 1-2-3/5 + V2_ref_notes, V3 notes + V3_ref_notes, V4 design section + V4_ref_notes (R1-R11), Y3 D_sigma.

## Design features and where they come from
- note def:SLD: (D0) ladder j, j0, disjoint infinite S_l, h_l = sum 2^{-s} e_s^*, delta_l = min{2^{-l},(4(1+||U||)||h_l||_1)^{-1}},
  dense targets y^(i) in c00 ∩ S_{q*}, y^(1) = e_{j0}^*/q*, schedule (i_r); (D1) allowedness (a),(b) WITH c_l FIXED BEFORE y_l;
  windows n^w_l, T_hi, T_lo, c_{l+1} = min{c_l/4, T_lo(l)^3}; (D2) T e_{k,m} = c_{j(k,m)} u_{j(k,m)}.
  thm:SLD: admissible + (P1),(P2),(P3). "Only (T-a)-(T-d), (P1)-(P3) used below."
- Y3 D_sigma: bounded gaps (S_l = {2^l(2i+1)}), allowedness (c): supp y ∩ S_{l'} ⊂ [1,l] for l' < l.
- Y1 D_X / Y4 D^PW / V1 D_Omega: M(l) = omega(l)+1 sub-windows, u(w) = b(w^-), Q(w) = (4 Design/u)^{omega+20},
  n(w) = ceil(l 2^{l^3} Q(w)), T_hi(w) = min{T_lo(w^-), 2^{-l^3}/(l Q)}, T_lo = 2^{-n} T_hi, b(w) = T_lo^4/(l Design);
  c_{l+1} = min{c_l/4, b(l,M(l))^2, (delta_{l+1}||h_{l+1}||_1)^2}; rate objects (R1)-(R7); Design(l) = [l 2^{l^3} 8^{sigma(l)}
  2^{s_max(l)} 2^{G(l)} delta_min^{-1} Lambda° (1+|T(l)|) D(l) G* H_comb G** H_tune Xi^Y]^6. DIAGONAL BASE s_j = 2^{-j}.
- V2 D^{V2}: determinantal objects (minors of A_kappa(v)), shift-pinning objects rho^sh (enlarged shift patterns, V2-ref P3),
  Design(l) *= Lip(l)(2+1/delta_comb(l))(rows cols)^l C_*(l), C_L(l) in Design, 1/delta_sh(l) in Design;
  b(w) = min{eta, (eta/C_L)^{N_L/2}}/(1+Lip C_*), eta(w) = T_lo^4/(l Design); c_{l+1} = min{c_l/4, T_lo(l,M)^3, b(l,M)^2}.
- V3 D^mu: diagonal base U k_s = mu_s e_s, mu_s = 2^{-s^2-1} (any mu_s in (0,1/2], -> 0; (RR) for power-law profiles needs
  super-exponential decay: with 2^{-s} only profiles |a| ~ v^{1+b}, b < 2, satisfy (RR)).
- V4 (+R6, R11): (SF*), (SF_tau) [tau_l decreasing -> 0], (b'), (Z0), (GM) [delta_l in [delta^max/2, delta^max]], (FD);
  ORDER per stage: S_l, y_l by (a) [schedule fixed in advance], delta_l by (GM), then c_l := minimum of all upper bounds,
  then level-l windows and Design.  (FD) only for the NEGATIVE Prop 5.8. Owners relative to L_N (R3) for row constructions.
- Rejected alternatives: Z3-ref EXPLOSIVE window function (superseded by pigeonhole; Y4 Prop 1.2); V4 Lemma 2.6 LACUNARY
  signature sets (conflicts with bounded gaps; (O4-crit) handled instead by D^mu + Theorem RS).

## Conflicts found (to be resolved in part 1)
 C1 base entries 2^{-j} (V1/V2) vs mu_s = 2^{-s^2-1} (V3).  V1 uses the value only via 8^{sigma(l)} (Lemma DR(ii), Lemma TU
    s'^2 v' >= 8^{-sigma}delta_min/2) and ||U|| = 1/2.  Fix: mu-base, replace 8^{sigma(l)} by B_mu(l) := 2^{sigma(l)}/mu_{sigma(l)}^2.
 C2 recursion order: note (c_l before y_l) vs V4-R6 (y_l, delta_l, then c_l).  Fix: R6 order; allowedness (b) enforced through c_l.
 C3 three different c_{l+1} formulas (V1, V2, V4).  Fix: minimum of all.
 C4 two b(w) (V1 vs V2).  Fix: V2's (smaller); no lower bound on b used anywhere (V2-ref).
 C5 lacunary vs bounded gaps; explosive vs pigeonhole.  Fix: bounded gaps + pigeonhole; nothing in MT II/III'/RS uses the others.
 C6 (FD) targets break "same target sequence in every block"; harmless (not a Lemma B requirement); keep schedule density.
 C7 V3 RS' stated over "SLD, D_sigma, SLD_G, D''', D_X, D^PW, D^Y" — not D_Omega/D^{V2}: needs the sub-window reading of (W*).
