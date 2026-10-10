# cert3 progress (cluster D: transfer to T_fin + window bookkeeping)

## Status
- [ ] read Q1 1.1-1.7 (T_fin definition, survival audit)
- [ ] read refa/refb on 1.7, P7, P8
- [ ] (2) inspection claims: X2 6.1, X1-ref 9 W'(4), U1-ref 6.3, U4 Lemma GW / II lem:II-GW
- [ ] (3) Part II tools: hypotheses vs T_fin
- [ ] (4) mu-base TU / DR(ii) / bank efficiency (U4 C1, 4.4(a))
- [ ] (5) window count P8 vs refb 1.7
- [ ] (6) P7
- [ ] (7) Part I with ||T|| = c_1 < 1
- [ ] write report

## Notes
- [x] read Q1 1.1-1.7, 2.x, 3.x; refa notes; refa part4 (P8); refb notes (1.7: "omega -> inf absorbs N-dep exponent").
- Part II T_final (def:II-Tfinal l.2057): base mu*_s=2^{-2^{2^s}}, FD targets at k(l) in K_FD={2^r} (fresh odd e_j), c_1:=1, Des(l) contains
  B*(l)=2^{s_t}/(delta_min mu*_{s_t}^2) with s_t = s_b + 2^{l+2}; Q(w)=(4Des/u)^{omega+20}; omega(l) >= 3l+|T(l)| (lem:II-ratescheme);
  patterns kappa=(E,P,eps,F',type), E subset [1,l] => #patterns >= 2^l; (O7) indexed by subsets of Ext(kappa) => omega >= 2^{|Ext|}-1 for II's cones.
- T_fin: no FD; absorber targets use fresh odd p_0..p_R > max T(l-1); every main stage followed by >=2 cluster stages => s_max(l) -> inf.
- KEY P8 worry: Q1's count D_cls=(J+1)3^J (A_max/eps)^p: exponent ~2Cp; p <= #minors <= omega(l) but need exponent >> 4Cp: omega+20 NOT enough
  unless refined pigeonhole (Caratheodory supp<=N) -> refa P8 needed. refb's "omega->inf absorbs" handles only N-dependence, not L/p-dependence.
- Part II def:II-DU1 (l.6703): Dbar(w)=(2L+1)3^{2L}(Des/u)^{C_Gamma(P(L)+2L+2)}, P(L)=2^{R_Gamma(L)}, R_Gamma=2|T(L)|+11L; Q(w):=max{Q,Dbar^3} at main stages.
  lem:II-classes (l.6986): J=|Omega|+N <= 2L since N <= L for L>=l_f (every block<=N has a carrier <= L); K_*<=(Des/u)^C; #classes, K_*^{J+2}, A_i <= Dbar.
  prop:II-ray(d) (l.7092): p <= P(L); (A_max/eps)^p <= (C_f Delta_max (Des/u)^{2C})^{P(L)} <= (Des/u)^{(2C+1)P(L)} once C_f Delta_max <= Des/u (L>=l_f).
  => Part II handles BOTH K_data (K_*^{J+2}) and C_f^p (absorbed via exponent P(L)) inside Dbar(w)^3.
- lem:II-scales(e) uses FD ONLY for s_max(l)->inf (=> eq:II-Finside F u T(l) in [1,s_max(l)] for l>=l_f); u(w),b(w)->0 FD-free.
  lem:II-scales(d) = prop:II-bank(c): (mu*_{s'})^2 v_c(s') >= Des^{-1/6} for s' <= s_t(l) (B* in Des).
- lem:II-GW: (GW1)-(GW4); (GW2) uses Q(w) >= (4Des/u)^{omega+20} and Des >= 2^{6 l^3} >= (l 2^{l^3} Lambda)^6. rem:II-GWuse: X_l = C^{l^2}(C/u)^{omega+8}Des^8 R_l.
- lem:II-TU (l.3703): base enters only via bank eff. (mu_{j'})^2 v(j') >= Des^{-1/6}, (mu_{j'} v(j'))^{-2} <= Des^{1/3}, v(j')>=Des^{-1/6} at j'=s'_{l''}(l)
  (first elt beyond s_max), + ||U||<=1/2, nu<=1, mu<=1 (||X_p||^2 <= sum p^2), 2^{G}<=Des^{1/6}, l<=Des^{1/6}, l 4^G <= Des^{1/2}; hyps (T1),(T2).
  T_fin (U4 C1): j' <= sigma(l) => mu_{j'}^2 v >= (4/5)delta_min/B_mu >= Des^{-1/6}; (mu v)^{-2} <= (25/16)(B_mu/delta_min)^2 <= Des^{1/3}. OK.
- Part II absorber subsection (l.6934-6941): standing "every constant <= C_f Dbar(w), absorbed by window since Q >= Dbar^3". Dbar used
  explicitly only in lem:II-classes, prop:II-ray(d), thm:II-MTIV proof (|S| >= n/Dbar^2 >= L2^{L^3}Dbar), cor:II-MTIVintr.
  lem:II-recursion/domfine/SCi/coststat/trueshift: NO explicit Q>=Dbar^3 use; they use (W2) at main stages, (W3), (W4'') with T_lo^3,
  block-1 ratio >= 8, n(k) >= Des(k) >= 1/(eta_k lambda_k) (P-R for T_fin), c_{L+1} <= T_lo^8, Lipschitz kappa <= Des/u.
## (ii) window count — analysis (draft)
- Q1 (S6) "C_U1 absolute" WRONG: K_data <= K_*^{J+2}K (zeroing J A_{J+1}Kt, projection H(L)); K_*<=(Des/u)^C => exponent ~C(J+2), J<=L+N
  (J<=2L once N<=L, i.e. L>=l_f with every block<=N having a carrier <= L = P7). Cube count (A_max/eps)^p, p up to P(L)=2^{R_Gamma(L)}.
- refb 1.7 ("omega->inf absorbs N-dependent exponent") incomplete: exponent grows with L (K_*^{J}) and with p (cone of level L), not only N.
  Rescue: omega(L) >= #(O5) ray components >= 2^L - 1 handles the C(L+N) part; the p part needs P8 (Caratheodory supp<=N) or Dbar.
- P8 precision: the cones Gamma^#(kappa,a) depend on f via ratio variables r in (X3), so "p_max(L)" must be the combinatorial bound
  P(L)=binom(R_Gamma,n-1)<=2^{R_Gamma(L)}; P(L) <= Design(L)^{1/2} anyway (2^{2|T|}<=2^{2 s_max}, 2^{11L}<=2^{6L^3}).
- Part II MT IV' proof wording "K of the form C_f(Des/u)^C" imprecise (K_data has K_*^{J+2}); correct reading K_data/c <= C_f Dbar(w)
  needs C_Gamma >= 2C + C_K + 2; then |S| c/K_data >= L2^{L^3}/C_f. OK.
- Option Dbar for T_fin: define R_Gamma(L) for X1-form cones (O(|T(L)|+L) rows), P(L), Dbar; Q:=max{Q,Dbar^3} at main stages; Q only grows.
- ||U||: T_fin 1/4 vs II 1/16 (nu <= ||U|| used in lem:II-donorraise(i) d_m <= Des^{1/3}Lambda/8 -> /2 with 1/4: constants only).
- II absorber rule e_r<2^{-R} ((mu*_{p0})^{2^{2^{p0}}-1}<2^{-R}) FAILS for mu-base (e_r ~ 2^{-p0^2} >> 2^{-2p0^2}c^2): only lem:II-zerovalue
  (route X, off tree). Flag for Q1 2.7 (route-X alternative claimed valid for T_fin): needs U1's own mu-base Lemma 3.3 argument.
## (iii) Part I under ||T||=c_1<1 — DONE (read proofs)
- Read: def:admissible, rem:lemmaA/B, Sec 1.2 (Phi_m(k)=2^{-m-k}q^*(Te)<=2^{-m-k}; L^*w = T(sum m2^{-m-k}w_m(k)e_{k,m}) exact for any T),
  lem:martintail (|R_m x|_m <= m2^{-m}q(x)), lem:rigidity (coef d_m s_k m2^{-m-k}, uses T-b,T-c), prop:forced (T-d), prop:smooth, prop:continuity,
  prop:approximants, prop:reduction, lem:pair (its "||T||=1" is the l_2^2 operator), lem:base, lem:block, lem:slack, lem:bookkeeping, lem:TV,
  prop:rebalancing, lem:transferdata (T-d tails), lem:persistence, lem:assembly, lem:approxfacts (sum_k lambda <= 1), lem:F1 (Phi_k<=2^{-k},
  sum Phi<=1), lem:anchor (C <= ||Phi||_2 < 1/2), def:SC, lem:scrambling, thm:engineered (Steps 0-6), lem:suplevel, lem:phicalc/switchbudget.
- Every use of T: (T-b),(T-c),(T-d) and UPPER bounds q^*(Te)<=1 (=> Phi<=2^{-m-k}, lambda<=m2^{-m-k}, ||Phi_m||_1<1, ||Phi_m||_2<1/2,
  ||R_m||<=m2^{-m}).  Equality clause / lower bounds on weights used only in: def:admissible, thm:SLD/(T-a) checks (l.2344, 3990), resonance
  example Sec 6 (l.2412-2415: Phi_m(1) for c_l=2^{-(l-1)^2}; off tree), cor l.3835 (off tree).  VERDICT: correct.
## (4) mu-base: U4 C1 re-derived: v_c(s)>=(4/5)delta_min 2^{-sigma}, mu_s^2 v_c(s)>=(4/5)delta_min/B_mu>=Design^{-1/6} (s<=sigma, mu decr.);
  (mu v)^{-2}<=(25/16)(B_mu/delta_min)^2<=Design^{1/3}; v>=Design^{-1/6}.  lem:II-TU proof uses only these + ||U||<=1/2, mu<=1, nu<=1 =>
  transfers verbatim (c_T=c_f Des^{-1}, C_T=C_f Des).  lem:II-bankformula exact for any diagonal base.  U4-ref tu_mu_hp (3000 bits) evidence.
  GW (U4 4.1) X_l allows only Design^8 and (C/u)^{omega+3}: K_data ~ (Des/u)^{C(2L+3)} is OUTSIDE GW's literal scope -> P8 needs own count.
## Transfer audit notes (Part II tools) — done reading
- Part II design interface used by tools on tree: (P1)-(P3) at main-stage sub-windows; allowedness (a),(c); S_l, bounded gaps; diagonal base
  identities (any diagonal base), ||U||<=1/2, mu<=1; bank eff. at FIRST element beyond s_max (finite F) [+ (D-lev) second element]; design
  domination lem:II-scales(c) / prop:II-bank(e) (uses G**(l), which T_fin's U4-Design contains; H_conf ~ Z4's G*(l), also in U4-Design);
  s_max->inf (eq:II-Finside); (W2) at main stages; (W3); (W4'') with T_lo^3; block-1 ratio>=8; absorber least entry (P-R); first touchers.
- lem:II-firsttouch for T_fin re-derived: no FD targets; absorber fresh p_i odd > max T(l-1); PRE pairs precede main targets meeting s in S;
  s in T(L) or S cap [1,L] lies in E^ch(L) (cluster right after L).  OK.
- lem:II-cost, lem:II-VT, lem:II-donorpeak, lem:II-status, prop:II-transplant, hoffman/loj, thm:II-B, lem:II-subset: no mu*/FD/c^low/B*/s_t use;
  ||U|| generic.  prop:II-transplant uses G**(l), Des^{1/3}Lambda (bank efficiency) -> T_fin OK.
- X2 6.1 claim "weights only through upper bounds" imprecise (absorber R, least entry eta_k (P-R), cluster capacity) — covered for T_fin by
  Q1 I2/I3/I6 + refb P-R.  X1-ref W4 list incomplete (misses P-R) — refb found it.
- P7 verified: L>=l_f => every block<=N has a coarse carrier (natural peak of Lemma M2) => N<=L, J=|Omega|+N<=2L; patterns of p_N among design
  patterns.  Presentational.
- refa part3 fix(a) omitted K_data's K_*^{J+2} (added in part4/notes 2.7). Final refa 2.7 consistent with my count.
- P(L)=2^{R_Gamma(L)} <= Design^{1/2} for T_fin (2^{2|T|}<=2^{2 s_max}<=Design^{1/3}, 2^{11L}<=Design^{1/6}) => P8 needs NO design change
  except dropping "C_U1 absolute"; omega(L) >= #(O5 components) >= 2^L - 1 handles O(L) exponent.
## numerics tu_mu_cert3.py (lem:II-TU proof transplanted to mu-base, 2500 bits)
- run 1 (eps_x = fac*reg, reg=min (s'v')^2): 58/90 ok; failures = negative bank masses for k=3 (G=16) even at fac=1e-4 — because the proof's
  kappa_T ~ (2^G eps_x)^2/reg: hypothesis eps_x <= c_T = c_f Des^{-1} requires the factor l 4^G, i.e. NOT a counterexample (hyp. violated).
- run 2 (eps_x = fac*reg/(l 4^G), the c_T scaling; Des >= l4^G (s'v')^{-2} holds in T_fin: Design^{1/2}>=l4^G, Design^{1/3}>=(s'v')^{-2}):
  90/90 ok for fac in 1e-4..10, smax 5..13 (banks j' up to 24, mu^2 = 2^{-1154}); |M'|<=0.125; val#-val2 = x to ~1e-600; banks>0;
  other carriers move O(eps_x^2/reg); T_fin design ineqs effOK/conOK in all runs.  Outputs: tu_mu_cert3.out (run 1), tu_mu_cert3b.out (run 2).
## OFF-TREE finding: route-X zero-value tuning (lem:II-zerovalue / U1 Lemma 3.3) for T_fin
- refB R11 (Part II) found U1 Lemma 3.3's left-endpoint gap; Part II's fix needs 4e_1 <= 2^{-R}, e_r = mu_{p_r}^2 theta_a/nu, achieved via
  doubly-exp base + p_0 rule ((mu*_{p0})^{2^{2^{p0}}-1} < 2^{-R}, using crude nu >= mu*_{p0} theta_a).
- T_fin (mu-base, p_0 = least odd > max T(l-1)): crude bound gives e_1 <= mu_{p1}^2/mu_{p0} = 2^{-p0^2-8p0-9} vs 2^{-R} ~ 2^{-2p0^2-8}c^2: FAILS.
  With true nu (f-const) and theta_a >= t|gamma_a| ~ C_f Des^2 lambda_a T_hi (no flips, prop:II-absorb(c),(d)): e_1/2^{-R} ~ 2^{-8p0}T_hi Des^2/(nu c)
  >> 1 (c <= exp(-1/T_lo)).  => Q1 2.7(a),(b) route-X "alternative/double coverage" and "alternatively 2.7(b)" in MT VI(b1) proof are NOT
  supported for T_fin as defined.  Possible fix: p_0 >= C log2(1/lb_l) (c^low independent of p_0) + perturbed-lattice rounding; or drop claims.
  MT VI (route V only) unaffected.
## FINAL: report written to ctx/r11/cert3_report.md (Sections 0-10).  window_count.py/.out added.
