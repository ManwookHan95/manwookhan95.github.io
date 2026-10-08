# P1 referee — part 3 (a new result: the defect mates are NOT recovered along the canonical truncations)

P1 (§0, §7.3) asserts that Thm 2.4 "shows that density cannot be proved by intrinsic (sequence-independent) recovery alone".
As written this does not follow: Thm 2.4 only shows g_{K1} is outside cl Cert^sh(f) (and all certificate-type classes); a mate
could still be recovered along EVERY NA sequence f_n -> f by some other mechanism. Below I prove the missing statement, for a
mild modification of P1's T. Setting: finite I containing 1, canonical base, notation of P1 §2.

## R1. Lemma (linear obstruction at C-tame approximants). PROVED (modulo C Thm 6.2 and C Prop 6.5, Round 1, unrefereed;
## I re-checked both proofs, and P1 3.8(a) at an NA point).
If f_n -> f in S_{p*} and every f_n is a C-tame NA point (a_n in c_00 automatically, K_n finite automatically, Qbar_{n,m} finite,
(MS) at x'_n), then Li_n C(f_n) is contained in Li_n S(f_n), where S(f_n) = (l_1(F_n) cap xhat_n^perp) + span{y^{(n)}_{k,m} : k in Q_{n,m}}.
Proof. C Thm 6.2 (Theorem A) gives C(f_n) in W(x'_n) (finite-dimensional); P1 3.8(a) (contact components vanish; the argument is
literally the same at an NA point: move the contact inward, correct with free coordinates, use (MS) and the overshoot bound C Lemma 5.2)
and C Prop 6.5 / Lemma 6.6 at x'_n (balance c_m = -d_m, b(x'_n) = 0; C Remark 6.7) give C(f_n) in S(f_n). QED.
Meaning: along C-tame approximants a mate g is recoverable only if g is a limit of the finite-dimensional certificate spans S(f_n);
for a switching mate that uses contacts, the approximants must carry base MASS on (a window of) those contacts — exactly the
"eta-trick"/window masses of A_referee §5.4 and P1 6.3 — or new non-peaks whose vectors approximate the switching part.

## R2. Modification (2.1') of P1's T. PROVED.
Fix an increasing sequence (N_n) and put z^{(n)} := e_1 + 1_{K' cap [1,N_n]} (finitely supported), x^{(n)} := z^{(n)} + U e in c_0.
For a non-special, non-exceptional l with target y_l = y^{(i)}, let Lambda(i) := {n : supp y^{(i)} meets K' cap (N_n, infinity)}
(finite). Replace the correction pi of 2.1 by pi_l := s_l alpha e_1*, where s_l is chosen with
  |s_l| <= 3 rho_l (2|Lambda(i)| + 3)   and   |(y_l + s_l alpha e_1*)(x)| >= 3 rho_l  for all x in {zhat} cup {x^{(n)} : n in Lambda(i)}
(possible: (alpha e_1*)(x) = alpha(1 + nu_1) = 1 for all these x, so the forbidden set for s is a union of |Lambda(i)|+1 intervals of
length 6 rho_l, and [-L, L], L = 3 rho_l(2|Lambda(i)|+3), is longer than their total length). Add to "i allowed at l" the condition
rho_l (2|Lambda(i)| + 3) <= min(rho_l^{1/2}, 1/(26(1+||U||))). Each i is still allowed at all large l (rho_l -> 0 along every block),
so (T-d) holds; pi_l is still supported on {1}, so the proof of (T-b),(T-c) is unchanged; n_l in [3/4, 5/4] and (P1)-(P3) hold as before.
New property (P4): for every n and every (k,m) != (2,1) with k >= 2, |u_{k,m}(x^{(n)})| >= 2 rho_l. Indeed if n in Lambda(i) this is the
choice of s_l (plus |delta_l h_l(x)| <= rho_l/2, h_l lives on S_l disjoint from K'); if n notin Lambda(i), x^{(n)} - zhat = -1_{K' cap (N_n,inf)}
is invisible to y_l, pi_l and h_l, so u_{k,m}(x^{(n)}) = u_{k,m}(zhat). Similarly u_{1,m}(x^{(n)}) = u_{1,m}(zhat) and exceptional vectors
are unchanged (targets supported on {1}).

## R3. Proposition (non-recovery along the canonical truncations). PROVED (modulo R1's imports).
With T as in R2, f as in P1 2.2, and f_n := grad p(x^{(n)}) (NA, attaining at x^{(n)}/p(x^{(n)})):
 (a) f_n -> f; (b) for n large, f_n is C-tame with Q_{n,1} = {2}, Q_{n,m} = empty (m != 1), no degenerate peaks;
 (c) C(f_n) is contained in the line R y^{(n)}, y^{(n)} := lambda_0 u - (Phi_1(2)^2 w^{(n)}_1(2)/C^{(n)}_1) R_1* w^{(n)}_1 -> lambda_0 u;
 (d) Li_n C(f_n) is contained in R u. Hence for every K_1 in K' with K_1 != empty, K' and every rho in (0,1], rho g_{K_1} is NOT in Li C(f_n):
     the explicit defect mates of Thm 2.4 are not recovered along (f_n). The fibre map C is not lower semicontinuous at f along (f_n).
Proof. (a) a(x^{(n)}) = alpha(1 + nu_1) = 1 and x^{(n)} in B_q, so grad q(x^{(n)}) = a; f_n = a + L* J_V(L x^{(n)}); x^{(n)} -> zhat weak*,
L x^{(n)} -> L** zhat in norm (L compact), J_V(L x^{(n)}) -> w weak*, L*J_V(L x^{(n)}) -> L* w in norm (A Fact E / G 6.6).
(b) Data at x'_n := x^{(n)}/p(x^{(n)}): q'_0 = 1/p(x^{(n)}), F = {1}, contacts K' cap [1,N_n] (finite), z^{(n)} in c_0. As in P1 2.2(b) with
(P2) and (P4): every (1,m) is a peak (|u_{1,m}(x')| >= 7 q'_0/9 > q'_0 2^{-m} >= |zeta'_m|/m), hence theta'_m Phi_m(k) <= q'_0 pi_{k,m}, and every
(k,m) != (2,1), k >= 2, is a peak with margin mu' >= q'_0 (2 rho_l - pi_{k,m}) >= q'_0 rho_l >= q'_0 sqrt(2 Phi_m(k)) (rho_l = sqrt(2Phi_m(k)/c_{l(1,m)})).
So no degenerate peaks, and (MS): sum_{mu' < s} Phi_m(k) <= sum_{Phi_m(k) < s^2/(2 q'_0^2)} Phi_m(k) <= s^2/q'_0^2 = o(s).
u(x^{(n)}) = u(zhat) - sum_{j in K', j > N_n} u_j = -tau_{N_n} -> 0, while theta'_1 Phi_1(2) -> theta_1 Phi_1(2) > 0; so for n large (2,1) is a strict
non-peak (with w^{(n)}_1(2) != 0, -> 0).
(c) By R1, C(f_n) in S(f_n); l_1({1}) cap xhat_n^perp = {0} (xhat_n(1) = 1 + nu_1 != 0) and the only strict non-peak is (2,1), so
S(f_n) = R y^{(n)}. (d) If g_n = gamma_n y^{(n)} -> g then gamma_n is bounded (||y^{(n)}|| -> lambda_0 ||u|| > 0), so g in R u. QED.

Remarks. (1) R3 makes P1's meta-claim rigorous (for the modified T): the defect mates are recovered (P1 6.3, SKETCH) only along
ENGINEERED sequences (masses on contacts), not along all sequences; "intrinsic" recovery in the strong sense (along every sequence,
as for cl Cert^sh by the Transport Theorem) fails. For P1's unmodified T the conclusion is very likely true but needs control of the
infinitely many targets that meet K' far out. (2) Consistency: 6.3's approximants put masses on the window contacts, so their
S(f') contains the window part of g' (l_1(F') cap xhat'^perp is then large) and the exact carrier gives y'_{2,1} = lambda_0 u: g' in S(f'),
as R1 demands.

## Numerical illustration (finite model, exact p* via SOCP; scripts refP1/model.py, t1_structure.py, t2_mates.py, t3_trunc.py)
Finite model of P1's example (U diagonal, 10 contacts, 14 free coordinates, one block with 7 coordinates; the special vector u has
u(zhat) = 0 and support {0} cup K'): forced data reproduce 2.2 (all block coordinates are peaks except the special one, where w = 0;
p*(f) = 1 = f(xi) to 1e-9). Two-piece mates g_{K1} (random K1, c = 0.05, 0.2): max_t [p*(f+tg) - s(t)] <= -3.7e-9 on a grid of 32 t-values
in [1e-4, 10] (gauge^2 between 0.008 and 0.26). A free-coordinate direction e_j* has first-order growth (p*(f+tg)-1)/|t| ~ 0.95-0.99 on
both sides (6.1 step (5)); a single-contact direction is a (scaled two-piece) mate direction: cost O(t^2) on both sides.
Canonical truncation f_N (contacts beyond N removed): the single-contact direction acquires FIRST-ORDER cost on the side t < 0
((p*-1)/|t| -> 0.045-0.07 for N = 8, ~1.9 for N = 5), and the discretized support max{g(x_*) : g in C(f_N)} drops from 0.20-0.40
(at f) to 0.04-0.06 (N = 8) and 5e-4 - 3e-3 (N = 5); the residual is the line R y^{(N)} (y^{(N)}(x_*) != 0 because w^{(N)}(2) != 0 in a
finite model) and grid effects. Consistent with R3.
